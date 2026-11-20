import pandas as pd
from sklearn.metrics import f1_score
# 리뷰 데이터셋
url = "https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/naver_shopping.txt"
df = pd.read_table(url, names=['rating', 'review']) # rating: 평점, review 리뷰
df = df[df['rating'] != 3] # 평점 3 제외

df['label'] = (df['rating'] >= 4).astype(int) # 4이상은 긍정
#전체데이터셋에서 특정 n개 샘플링
df_sample = df.sample(n=5000, random_state=42).reset_index(drop=True)
print(df_sample.shape)

import re 
cleaned_list = []
for text in df_sample['review'] :
    #re.sub()
    text = re.sub(r'[^가-힣a-zA-Z0-9\s]',' ',str(text) )
    #.join(리스트) : 각 리스트 항목 사이에 특정 문자 연결
    # .split(): 하나의 문자열내 특정 문자로 분리하여 리스트 반환
    cleaned_text = ' '.join( text.split() )
    cleaned_list.append(cleaned_text)
df_sample['cleaned_review'] = cleaned_list
print(df_sample.head(3) )

#2 한국어 형태소 분석기 , kiwi
# pip install kiwipiepy
from kiwipiepy import Kiwi
kiwi = Kiwi()
for word in ['가성비','내돈내산','총알배송']: # 3. 사전학습에 없는 단어 추가
    #kiwi.add_user_word
    kiwi.add_user_word(word, 'NNG')

#4 불용어: 핵심 의미가 없는 형태소를 1차적으로 걸러내기 위해
from kiwipiepy.utils import Stopwords
kiwi_stopwords = Stopwords()
custom_stopwords = {'그냥','그저','모른다'}
#5. kiwi 이용한 형태소 분석 점수
def tokenize_kiwi(text) :
    # kiwi.tokenize(분석할 문장, stopwords=불용어 객체)
    tokens = kiwi.tokenize(text, stopwords=kiwi_stopwords)
    # 추출할 품사 키워드, NNG 일반 명사, NNP고유명사, VV동사
    target_tags = {'NNG', 'NNP', 'VV', 'VA', 'MAG'}
    result = []
    for t in tokens : # 토큰나이즈가 된 리스트에서 원하는것만 필터링 /추출
        #t.tag : 품사, t.from 형태소 문자열 반환
        if t.tag in target_tags and t.tag not in custom_stopwords : # 내가 원하는 품사에 포함된 단어이면
            if len(t.form) > 1 or t.form in {'못','잘'} : # 일부 제외한 한단어 제외
                # 동사와 형용사 어간 뒤에 다 붙인다. 좋고 좋아서 좋네요 -> 둘다 
                word = t.form + '다' if t.tag in { 'VV', 'VA' } else t.form
                result.append(word)
    return result

test_word = df_sample['cleaned_review'].iloc[0]
print(test_word)
print(tokenize_kiwi(test_word))

########전처리: 학습 하기전에 문장들을 단어로 분리
#6. 특성과 타깃 분리
from sklearn.model_selection import train_test_split

X_train, X_test,Y_train,Y_test = train_test_split(
    df_sample['cleaned_review'],df_sample['label'],
    random_state=42, test_size=0.2, stratify=df_sample['label'] 
)
#7. 리뷰--> 행렬(백터) 변환
from sklearn.feature_extraction.text import TfidfVectorizer
# TFidfVectorizer(tokenizer = 토크나이즈 함수)
tfidf = TfidfVectorizer(
    tokenizer=tokenize_kiwi, # 생략시 공백 /띄어쓰기 기준으로 분리  직접 만든 함수
    token_pattern=None, # 실행중 발생 하는 로그 비활성화
                        )
X_train_tfidf = tfidf.fit_transform(X_train) #학습 -> 변환 # 학습용
X_test_tfidf = tfidf.transform(X_test) #테스트용

print( X_train_tfidf.shape)
print( X_test_tfidf.shape)

# (4000, 4108)
# (1000, 4108)

print('추출한 단어 10개만 확인:', tfidf.get_feature_names_out()[:10])
# 추출한 단어 10개만 확인: ['가게' '가겨' '가격' '가격대' '가관' '가구' '가까이' '가끔' '가늘다' '가능']

#문제점: 오타 분별 불가능
# (해결) 유사도 거리 계산 (임베딩/BERT)

#8. 긍정/부정 : 감성 분석
from sklearn.linear_model import LogisticRegression # 실무적으로 lightGBM
model = LogisticRegression(
    C=0.1,
    max_iter=1000,
    random_state=42
)
model.fit(X_train_tfidf, Y_train) # 분류 모델 학습
print(model.score(X_train_tfidf, Y_train)) #0.803
print(model.score(X_test_tfidf, Y_test))  #0.794
Y_pred = model.predict(X_test_tfidf)
print('f1:', f1_score(Y_test, Y_pred))  #f1: 0.7799145299145299

#9. 예츠갛기
print(X_train_tfidf.toarray()[0]) #수치 행렬


new_reviews = [
    "배송도 정말 빠르고 가성비 최고입니다! 재구매 의사 있어요.",
    "마감 상태가 엉망이고 실밥이 다 터져서 왔네요. 최악입니다.",
    "그냥 가격만큼 하는 것 같아요. 특별히 좋지도 나쁘지도 않음."
]

cleaned_new =[]
for text in new_reviews:
    text = re.sub(r'[^가-힣a-zA-Z0-9\s]', '',str(text))
    cleaned_new.append(' '.join(text.split()))
    #정규 표현식 이후 토큰나이즈
new_tfidf = tfidf.transform(cleaned_new)
    #토크나이즈 이후 모델 추론
probs = model.predict_proba(new_tfidf) 

for i in range(len(new_reviews)) :
    pos = probs[i][1]
    if pos >= 0.6 :
        contents= '긍정'
    elif pos <=0.4: 
        contents = '부정'
    else :
        contents = '중립'
    print( f'리뷰: , {new_reviews[i]}')
    print( f'감성분석: , {contents}, 긍정확률:{pos}, 부정확률:{probs[i][0]}') 

# 리뷰: , 배송도 정말 빠르고 가성비 최고입니다! 재구매 의사 있어요.
# 감성분석: , 긍정, 긍정확률:0.7491070811952683, 부정확률:0.25089291880473175
# 리뷰: , 마감 상태가 엉망이고 실밥이 다 터져서 왔네요. 최악입니다.
# 감성분석: , 부정, 긍정확률:0.30126014210492447, 부정확률:0.6987398578950755
# 리뷰: , 그냥 가격만큼 하는 것 같아요. 특별히 좋지도 나쁘지도 않음.
# 감성분석: , 부정, 긍정확률:0.363768990226901, 부정확률:0.636231009773099

