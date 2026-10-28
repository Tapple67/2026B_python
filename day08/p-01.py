# 판다스 : 데이터 조작 및 분석(표형태) 라이브러리
#성치 : pip install pandas
# 호출/ 버전 확인
import pandas as pd

print(pd.__version__)

#1] 데이터 프레임 : 2차원 (표)


data_list = [ [ 'ant' , 25 , 'seoul'] ,
            ['bee' , 30 , 'busan'] ,
            ['cat' , 35 , 'incheon'] ] # 2차원 리스트 

x = pd.DataFrame(data_list)
print(x) # 행 과 열 => 표 형식
x= pd.DataFrame(data_list, columns=['name', 'age', 'city'])
print(x)

#2] 데이터 프레임2, pd.DataFrame(딕셔너리), 키 (열 이름)
data_dict = { 
  'name' : ['ant','bee','cat'] , 
  'age' : [25,30,35] , 
  'city' : ['seoul','busan','incheon'] } # 딕셔너리


df= pd.DataFrame(data_dict)
print(df)

#3] 컬럼 값 추출, df['열이름']
ages = df['age']
print(ages)
print(type(ages))
print(type(ages.values))

# 4] 데이터프레임3 : 넘파이
import numpy as np
data_np = np.array(data_list) # 넘파이 자료
df = pd.DataFrame(data_np , columns= ['name', 'age', 'city'], index=['A','B','C'])
print(df)

# 5] 주요속성
print(df.shape) #행/열 크기 # (3,3)
print(df.columns) # 컬럼 목록 Index(['name', 'age', 'city'], dtype='str')
print(df.index) # 인덱스 목록 Index(['A', 'B', 'C'], dtype='str')
print(df.head(2)) # 상위 n개만 반환
print(df.tail(2)) # 하위 n개만 반환

df.info() # 컬럼이름, 결측치, 타입 확인
    #   Column  Non-Null Count  Dtype
#  ---  ------  --------------  -----
#   0   name    3 non-null      str  
#   1   age     3 non-null      str  
#   2   city    3 non-null      str

# 6] 인덱싱 = iloc.[행인덱스,열인덱스]/ 슬라이싱
print(df.iloc[1]) # 1행
print(df.iloc[1,2]) #busan
print(df.loc['B'])

print(df.loc['B', 'city']) # B행 city열

df['age'] = df['age'].astype(int)

#7] 슬라이싱, [시작인덱스:끝인덱스], [행슬라이싱, 열슬라이싱]
print(df.iloc[0:2, 0:1])
print(df.loc['A':'C','name':'age'] )

#8] 열 추가, df[새로운컬럼] = 새로운 값
df['score'] = [100, 80, 95]
print(df)

df.loc['B','age'] = 70
print(df)

df.iloc[0,0] = 'apple'
print(df)

#10] 여러개 수정, [[특정인덱스]]
df.loc[['A','B'], 'score' ] = [50, 60]
print(df)

#11] 필터링(조건) 
cont = df['age'] >= 40

print(df[ (df['score']>70) & cont])
print(df[ (df['score']>70) | cont])

#필터링 이용하여 새로운 열
df.loc[df['score']>70, 'passed'] = True

print(df)

#12] 컬럼명 변경, df.rename(columns={'기존열이름' : '새로운컬럼명'})
df = df.rename(columns={'city': '도시','age': '나이' })
print(df)
df.info
#13] 집계, df.describe(), df['열이름'].통계함수()
print("13-1", df.describe())
print("13-2", df['나이'].sum())
print("13-3", df['passed'].value_counts() ) # 자료 빈도 수

#14] 합치기/병합
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Score': [90, 80, 85]})
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Score': [75, 95, 88]})

#세로 연결axios pd.concat([df1, df1], axis = 0세로 연결 1 가로연결, ignore_index = True )
new_df = pd.concat([df1, df2], axis = 0, ignore_index=True)
print(new_df)
new_df = pd.concat([df1, df2], axis= 1 )
print(new_df)

# 병합
df_info = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})
df_score = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})

new_df=pd.merge(df_info, df_score, on='ID', how='inner')
print(new_df)


new_df=pd.merge(df_info, df_score, on='ID', how='outer')
print(new_df) #NaN : 정의가 없는 자료 # 숫자가 아니다

#15] 정렬,  df.sort_values(by = '컬럼명', ascending=False 오름차순/Fasle내림차순 )
df = pd.DataFrame({
  'name': ['Ant', 'Bee', 'Cat', 'Dog'],
  'age': [27, 27, 22, 32],
  'score': [88, 95, 85, 90]
})

# df.sort_values(by = '컬럼명', ascending=False )
print(new_df)
# 다중 정렬은 []리스트 사용, * age 기준으로 1차 정렬후 동일한 age 끼리 score 기준으로 2차 정렬
new_df = df.sort_values(by = ['age', 'score'], ascending=[True,False])
print(new_df)
# 컬럼명도 정렬이 가능하다. axis = 0행/1열
new_df = df.sort_index(axis= 1 , ascending=True)
print(new_df)

