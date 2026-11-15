# 부스팅 앙상블 
#설치 : pip install lightgbm xgboost


url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'

import pandas as pd

df = pd.read_csv(url)

X = df[['alcohol','sugar','pH']]
Y = df['class']

from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

#3가지 부스팅 앙상블 사용, xx
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

models = {
    "XGBoost" : XGBClassifier(n_estimators = 1000, learning_rate = 0.05, max_depth=4,random_state=42, n_jobs=-1),
    "lightgbm" : LGBMClassifier(n_estimators = 1000, learning_rate = 0.05, max_depth=4, random_state=42,  n_jobs=-1, verbose =-1)
}

#2) 반복 이용하여 모델 학습 / 학습 시간 테스트
import time
for name, model in models.items() :
    start = time.time()
    model.fit(X_train, Y_train)
    end = time.time() - start

    Y_pred = model.predict(X_test)

    print("===========모델명: ", name)
    print("> 학습 소요 시간: ", end , '초')
    print("> train acc : ", model.score(X_train,Y_train))
    print("> test acc : ", model.score(X_test,Y_test))
    print("> f1 score : ", f1_score(Y_test, Y_pred, average="macro") )



