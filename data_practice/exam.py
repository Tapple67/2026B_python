import numpy as np
# [기본 제공 코드] CSV 파일 로드 (헤더 제외, 콤마 구분)
data = np.genfromtxt('./pred_food.csv', delimiter=',', skip_header=1, dtype=str, encoding='utf-8-sig')

# 데이터 구조 확인: [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]
print(f"데이터 형태: {data.shape}")

np.set_printoptions(suppress=True, precision=2)

# row1 = data[1,:]
# print(row1)

# foodindex = data[:,0].argsort()
# print(data[foodindex])


# print( data[data[:,1] < 5] )

high = data[(data[:,1].astype(float) >= 70) | (data[:,3].astype(float) >=50)]

# print(len(a))


Carbohydrates = data[:,3]
# print(Carbohydrates)

GI = data[:,1]
# print(GI)

GL = (Carbohydrates.astype(float) * GI.astype(float))/100 
# print(GL)
max_GL = np.argmax(GL)
# print(max_GL)

# 정규화 = (sales - np.min(sales) / np.max(sales) - np.min(sales))

# 정규화 = (GL - np.min(GL)) / (np.max(GL) - np.min(GL))
# print(data[정규화>=0.9])
# high_gl_names = data[GL >= 20, 0]
# print(high_gl_names)

temp = np.column_stack((GL, data[:, 1].astype(float)))

# 조건 마스크 생성
condition = (temp[:, 0] >= 20) & (temp[:, 1] >= 70)
result = temp[condition]

# 비율 출력
print(len(result) / len(data) * 100, "%", sep="")

# result의 0번 열(GL) 기준 내림차순 정렬 후, 조건에 맞는 음식 이름(data[condition, 0])에서 상위 7개 추출
top7_names = data[condition, 0][np.argsort(result[:, 0])[::-1][:10]]
print(top7_names)

# 1. 음식 이름(0번), GL(1번), GI(2번) 병합
temp = np.column_stack((data[:, 0], GL, data[:, 1].astype(float)))

# 2. 조건 필터링 (GL 20 이상 AND GI 70 이상)
result = temp[(temp[:, 1].astype(float) >= 20) & (temp[:, 2].astype(float) >= 70)]

# 3. 2번 열(GI) 기준 내림차순 정렬 후 상위 7개 음식 이름(0번 열) 추출
top7_names_by_gi = result[np.argsort(result[:, 2].astype(float))[::-1][:7], 0]

print(top7_names_by_gi)


