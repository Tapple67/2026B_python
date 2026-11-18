# 지도학습 : X특성(독립)과 Y 타깃(종속) 모델에 학습하여 예측
# 비지도 학습: X특성(독립) 모델 이용하여 거리/ 밀도 구집/클러스터/그룹

import pandas as pd
url = "https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv"
df = pd.read_csv(url, sep=';')

X = df[['studytime', 'absences', 'G1', 'G2', 'G3']] #공부시간, 결석 일수, 1학기 성적~3학기성적

# 타깃/ 종속 없다. -> 비지도 학습 이라서
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split #학습 98% 검증용2% ( 중요도 떨어짐)
X_train, X_test = train_test_split(X, test_size=0.02, random_state=42)

#1) 스케일링/단위표준화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train) # fit + transform => fit_transform
X_test_scaled = ss.fit_transform(X_test)
#2) 군집 = 그룹 만들기 = 클러스터

from sklearn.cluster import KMeans
model = KMeans(n_clusters=5) # 모델 생성 #주의할 점: 만약 최대학생10명일때 클러스터 수가 10개이면 의미가 없어진다.
model.fit(X_train_scaled) # 군집 학습
train_labels = model.predict(X_train_scaled) #군집추론
print('앞에서 10명 그룹 확인:', train_labels[:10])
print('테스트 학생: ', model.predict(X_test_scaled))

# 시각화 : 특성 여러개 이므로 2d 시각화 한계 
# 판다스 복습
list_2 = [[2,3],[4,5]]
# print(list_2[ : 1]) [[2,3]] #리스트[시작행:끝행 -1]
# print(list_2[ : , 1]) # 리스트 [ 행 : 열] # 생략시 전체 => 전체행에 첫번째 열 # 판다스 /넘파이 제공


import matplotlib.pyplot as plt
plt.scatter(X_train_scaled[:, 4], X_train_scaled[:, 1], c=train_labels)
plt.scatter(X_test_scaled[ : , 4],X_test_scaled[ : , 1], c='red', marker='*')
# plt.show()



#4) 최적의 K(군집/그룹) 수 찾기 VS 지도 학습( F1/R2)
sse_list = []
sil_list =[]
for k in range(2,20) :
    k_temp = KMeans(n_clusters=k, random_state=42)
    preds = k_temp.fit_predict(X_train_scaled) # 모델 학습/추론 동시에 , fit + predict
    sse_list.append(k_temp.inertia_) # 군집 결과에 각 샘플과 중심점 거리 제곱의 합 저장
    sil_list.append(silhouette_score(X_train_scaled, preds))

plt.plot(range(2,20), sse_list ,marker='o')
# plt.show()
plt.plot(range(2,20), sil_list ,marker='o')
# plt.show()
#sse = 엘보우지점(기울기가 완만하게 꺽이는 변곡점) 5~10
# 실루엣 : 높은 값일 수록 이상적
# 두 차트 해석하여 최적의 K해석
# 최적 k 군집하기
best_model = KMeans(n_clusters=5)
pred = best_model.fit_predict(X_train_scaled)
print(pred[:10])
# [1 3 3 0 2 0 3 0 0 0]

# 5) HDBSCAN # k-means 다르게 밀도 기반으로 군집, 이상치(-1) 자동탐지

from sklearn.cluster import HDBSCAN
model = HDBSCAN(min_cluster_size=15, min_samples=5)
pred = model.fit_predict(X_train_scaled)
print(pred) # 군집/그룹 4개, 이상치 1개(-1)

X_train['hdb_cluster'] = pred
print(X_train['hdb_cluster'].value_counts())
# 0, 194, 1 85, 2, 56, -1, 32, 3 20
# min_cluster_size, min_samples 15, 5 -> 30,2
# 1, 1842,2 89,0 81,-1 33
# 시각화 :
noise_mask = (X_train['hdb_cluster']==1)
plt.scatter(X_train.loc[~noise_mask,'G3'], X_train.loc[~noise_mask,'G3'], c=X_train.loc[~noise_mask,'hdb_cluster'])
plt.scatter(X_train.loc[noise_mask,'G3'], X_train.loc[noise_mask,'G3'], c='red',marker='*')


plt.show()

#6)PCA(주성분 분석) : 고차원 데이터의 분산을 저차원으로 축소하여 주성분/특성 만들기
#고차원이란? 다수의 특성들의 가중치/기울기 표현, 상관계수란? A특성과 B특성의 관계성 (A가 변경되면 B 얼마나 변하는지 관계성을 수치로 나타냄)
from sklearn.decomposition import PCA
# PCA( n_components=차원수)
pca = PCA( n_components = 2) # 시각화(2d) 하기 위해
## 딥러닝(이미지 3차원)
X_train_pca = pca.fit_transform(X_train_scaled)
print(X_train_pca)
print(pca.components_.T)

#     주성분1       주성분2           
# [[ 0.13219328 -0.61408979]        공부시간
#  [-0.00599139  0.78051288]        결석일수
#  [ 0.56213845  0.00343157]        1학기 성적
#  [ 0.58342273  0.03443535]        2학기 성적
#  [ 0.57105808  0.11178463]]       3학기 성적

pca_hdb = HDBSCAN(min_cluster_size=30, min_samples =5)
pca_pred = pca_hdb.fit_predict(X_train_pca)

X_train['PC1'] = X_train_pca[: ,0]
X_train['PC2'] = X_train_pca[: ,1]
X_train['PCA_cluster'] = pca_pred
print(X_train[ ['PC1','PC2','PCA_cluster'] ].head(10))


# 316 -2.221877 -0.804689           -1
# 116  0.808827 -0.220407            2
# 9    1.758814 -0.368879            2
# 209 -1.525153 -0.789537           -1
# 323  1.417209 -1.011025           -1
# 393  0.000504  0.206730            0
# 258  1.644120  0.375856           -1
# 155 -0.714701 -0.412403            1
# 124 -1.381884 -0.619013           -1
# 272  0.124762 -0.311819            1

#7) 이상치 제외한 G3평균
normal_clusters =X_train[X_train['PCA_cluster'] != -1] #이상치 제외
cluster_means = normal_clusters.groupby('PCA_cluster')['G3'].mean()
sorted_cluster = cluster_means.sort_values(ascending = True) # True 오름차순
print( sorted_cluster )

# PCA_cluster
# 1     9.873239
# 0    12.513514
# 2    13.641509

#8) 라벨링
labels = { }
for idx, cluster_id in enumerate(sorted_cluster.index, start=1):
    labels[cluster_id] = f'Level{idx}'
labels[-1] = 'Outlier' # 이상치는 리스트 가장 뒤에 
print(labels)

# {1: 'Level1', 0: 'Level2', 2: 'Level3', -1: 'Outlier'}
X_train['pca_cluster_label'] = X_train['PCA_cluster'].replace(labels)
print(X_train)

#      studytime  absences  G1  G2  G3  hdb_cluster       PC1       PC2  PCA_cluster pca_cluster_label
# 316          2         0   8   8   0            0 -2.221877 -0.804689           -1           Outlier
# 116          2         2  11  13  14            0  0.808827 -0.220407            2            Level3
# 9            2         0  14  15  15            0  1.758814 -0.368879            2            Level3
# 209          3         6   7   7   7            2 -1.525153 -0.789537           -1           Outlier
# 323          3         1  12  14  15            2  1.417209 -1.011025           -1           Outlier
# ..         ...       ...  ..  ..  ..          ...       ...       ...          ...               ...
# 71           4         0  10  10  10            3 -0.011215 -1.996772           -1           Outlier
# 106          4         8   7   8   8            3 -1.090101 -1.289742           -1           Outlier
# 270          2        15   9   9   9            0 -0.786760  0.882016            1            Level1
# 348          3         0  13  15  15            2  1.744444 -1.097961           -1           Outlier
# 102          1         4  10  13  14            1  0.479520  0.700890            0            Level2

# 지도 학습에서 성능 향상 하기위한 방법: 0) 전처리 1)하이퍼파라미터 2) 파생변수 
# 자바 활용 방법: 관리자 페이지 해당 회원이 위험군/VIP 

#9) 시각ghk
for lbl in list(labels.values() ) :
    sub = X_train[X_train['pca_cluster_label']==lbl]
    if lbl =='outlier' :
        plt.scatter(sub['PC1'], sub['PC2'], c='red', marker="*", label=lbl)
    else:
        plt.scatter(sub['PC1'], sub['PC2'], marker="o", label=lbl)
plt.legend()
plt.show()