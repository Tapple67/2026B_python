import pandas as pd


df = pd.read_csv("./SeoulBikeData.csv")

# df.info()

#8760행

#  #   Column                   Non-Null Count  Dtype  
# ---  ------                   --------------  -----  
#  0   Date                     8760 non-null   str       dayofweek  -> OneHotEncoder
#  1   Rented Bike Count        8760 non-null   int64                               수
#  2   Hour                     8760 non-null   int64     OneHotEncoder             시간 
#  3   Temperature              8760 non-null   float64   StandardScaler 표준화     온도
#  4   Humidity(%)              8760 non-null   int64     StandardScaler 표준화     습기
#  5   Wind speed (m/s)         8760 non-null   float64   StandardScaler 표준화     풍속
#  6   Visibility (10m)         8760 non-null   int64     StandardScaler 표준화     가시거리
#  7   Dew point temperature    8760 non-null   float64   StandardScaler 표준화     이슬점 온도
#  8   Solar Radiation (MJ/m2)  8760 non-null   float64   MinMaxScaler   정규화       태양 복사량
#  9   Rainfall(mm)             8760 non-null   float64   StandardScaler 표준화     강우량 
#  10  Snowfall (cm)            8760 non-null   float64   StandardScaler 표준화     적설량
#  11  Seasons                  8760 non-null   str       OneHotEncoder             계절
#  12  Holiday                  8760 non-null   str       OneHotEncoder(drop='if_binary')   공휴일
#  13  Functioning Day          8760 non-null   str       빼기                          정상운영여부
df['dayofweek'] = pd.to_datetime(df['Date'], dayfirst=True).dt.dayofweek
df = df.drop(columns=['Date'])
df = df.drop(index= df[df['Functioning Day']=='No'].index )
X = df.drop(columns=['Functioning Day'])

X.info()
Y= df['Rented Bike Count']
Y.info()

from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
# 데이터 분할
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder, PolynomialFeatures

num_cols = ['Temperature','Humidity(%)','Wind speed (m/s)','Visibility (10m)','Dew point temperature','Rainfall(mm)','Snowfall (cm)']
cat_cols = ['Hour','Seasons','dayofweek']
ho_cat_cols = ['Holiday'] # drop='if_binary'
minmax_cols = ['Solar Radiation (MJ/m2)']

#전처리
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_cols),
    ('ho_cat', OneHotEncoder(drop='if_binary'), ho_cat_cols), #이진 변수만 줄임
    ('minmax', MinMaxScaler(), minmax_cols),
])

from sklearn.pipeline import Pipeline
#파이프
pipeline = Pipeline([
    ('prep', preprocessor),              # 앞단: 전처리
    ('poly', PolynomialFeatures()),      # 중간: 피처 확장 (선택)
    ('Ridge', Ridge())
])

# Kfold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

param_grid = {
    'poly__degree': [1, 2],
    'Ridge__alpha': [0.1, 1.0, 10.0]
}


#GridSearchCV
grid = GridSearchCV(
    estimator=pipeline,  # <-- 여기에 전체 파이프라인을 통째로 넣음
    param_grid=param_grid,
    cv=kfold,                 # <-- 여기에 KFold를 넣음
    scoring='r2',
    n_jobs=-1
)

# 테스트
grid.fit(X_train, Y_train)

model = grid.best_estimator_

y_pred = model.predict(X_test)

from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score

print(f"검증(CV) RMSE : {-grid.best_score_:.2f}")
print(f"테스트 RMSE   : {root_mean_squared_error(Y_test, y_pred):.2f}")
print(f"테스트 MAE    : {mean_absolute_error(Y_test, y_pred):.2f}")  # 평균적으로 몇 대 정도 틀리는지 직관적 확인
print(f"테스트 R2     : {r2_score(Y_test, y_pred):.4f}")

# 검증(CV) RMSE : -0.84
# 테스트 RMSE   : 255.87
# 테스트 MAE    : 163.88
# 테스트 R2     : 0.8332

import joblib
# joblib.dump(model,'./bike_model.pkl')

model= joblib.load('./bike_model.pkl')

sample_data = pd.DataFrame([
    # [시나리오 1] 맑은 가을 평일(수요일) 오후 6시 퇴근길 -> 대여량 높게 예측되어야 정상
    {
        'Hour': 18,
        'Temperature': 21.5,
        'Humidity(%)': 48,
        'Wind speed (m/s)': 1.5,
        'Visibility (10m)': 2000,
        'Dew point temperature': 10.0,
        'Solar Radiation (MJ/m2)': 0.45,
        'Rainfall(mm)': 0.0,
        'Snowfall (cm)': 0.0,
        'Seasons': 'Autumn',
        'Holiday': 'No Holiday',
        'dayofweek': 2
    },
    # [시나리오 2] 영하의 추운 겨울 평일(월요일) 새벽 3시 -> 대여량 매우 낮게 예측되어야 정상
    {
        'Hour': 3,
        'Temperature': -5.2,
        'Humidity(%)': 40,
        'Wind speed (m/s)': 2.8,
        'Visibility (10m)': 1800,
        'Dew point temperature': -16.5,
        'Solar Radiation (MJ/m2)': 0.0,
        'Rainfall(mm)': 0.0,
        'Snowfall (cm)': 0.0,
        'Seasons': 'Winter',
        'Holiday': 'No Holiday',
        'dayofweek': 0
    },
    # [시나리오 3] 비 오는 여름 공휴일(일요일) 오후 2시 -> 강수량 영향으로 낮게 예측되어야 정상
    {
        'Hour': 14,
        'Temperature': 26.0,
        'Humidity(%)': 92,
        'Wind speed (m/s)': 3.4,
        'Visibility (10m)': 600,
        'Dew point temperature': 24.5,
        'Solar Radiation (MJ/m2)': 0.15,
        'Rainfall(mm)': 8.5,
        'Snowfall (cm)': 0.0,
        'Seasons': 'Summer',
        'Holiday': 'Holiday',
        'dayofweek': 6
    }
])


preds = model.predict(sample_data)

for i, pred in enumerate(preds, 1):
    print(f"시나리오 {i} 예측 대여량: {pred:.1f}대")
