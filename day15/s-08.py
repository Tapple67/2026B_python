# 범주형(문자) 특성 갖는 학습 방법 

# 1) 
import seaborn as sns
df = sns.load_dataset('penguins')       # 안에 있는 더미데이터 
df.info()

# 2) 전처리 : 결측제외 
df = df.dropna().reset_index(drop=True)   # ← 결과를 df에 다시 저장
df.info()

# 3) 다중분류 실습 위한 특성/타깃
X = df.drop(columns=['species'])    # 펭귄 중 제외한 나머지 특성
Y = df['species']

# 4) 분리
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42, stratify= Y)

# 5) 복합형 파이프라인 위한 수치형과  범주형  특성분리 
num_features = ['bill_length_mm' , 'bill_depth_mm','flipper_length_mm','body_mass_g']
cat_features = ['island' , 'sex']

#6) 복합 특성
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
# pp = ColumnTransformer(transformers=['식별자', '전차리기','컬럼목록'])

pp = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_features), 
    ('cat', OneHotEncoder(drop='first', sparse_output=False), cat_features )
    ])

#파이프라인 만들기
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

#pipe = Pipeline (['식별자' , 변환기/추점기])
pipe = Pipeline([('pp',pp), ('model',LogisticRegression() )])

#학습하기
pipe.fit(X_train, Y_train)

Y_pred = pipe.predict(X_test) 
print( Y_pred[:3] )

from sklearn.metrics import f1_score
print(f1_score(Y_test, Y_pred, average='macro'))
