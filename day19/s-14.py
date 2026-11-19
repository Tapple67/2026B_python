import pandas as pd
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
def tokenize_with_kiwi(text) :
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
print(tokenize_with_kiwi(test_word))

#########################################