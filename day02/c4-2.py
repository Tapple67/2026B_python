# p.217 딕셔너리;
# 딕셔너리란? {} 중괄호 선언하고 키:값 형태로 쉼표 연결
# {key:value, key:value, key:value}
# key 중복x / value 중복

dict_a = {'name' : '어벤져스 엔드게임', 'type' : '히어로 무비'}
print(dict_a['name']) # 어벤져스 엔드게임
print(dict_a['type']) # 히어로 무비

# 3. 값추가, 딕셔너리명['새로운 키'] = 새로운값
dict_a['price'] = 5000
print (dict_a)
dict_a['type'] = '호러무비' # 이미 존재 하는 키는 수정

print(dict_a)

#5. 속성 삭제, del
del dict_a[ 'price' ]
print(dict_a)

#6. 딕셔너리 내부 확인, 찾을키 in 딕셔너리명
print('price' in dict_a)
print('name' in dict_a)

#7. 속성값 호출, 방법1: 딕셔너리명['key'] , 방법2: 딕셔너리명.get(key)
# 차이점: 방법1은 존재하지 않으면 예외발생, 방법2는 존재하지 않으면 None 반환 
print(dict_a.get('name')) # 어벤져스 엔드게임
print(dict_a.get('price')) # None

#8. for 반복문과 딕셔너리, 딕셔너리 내 key 하나씩 for문에서 순회
# for key 반복변수 in 딕셔너리명:
    #실행코드
for key in dict_a:
    print(dict_a.get(key)) #방법1
    print(dict_a[key] ) #방법2

dictionary = { 
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕","메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

for key in dictionary:
    for key, value in key.items():
        print(key,":",value)




lst = [1,2,3]
dst = {i : i * 2 for i in lst}
s = set(dst.values())
lst[0] = 99
dst[2] = 7
s.add(99)
print(len(s & set(dst.values())))

numbers = [273, 103, 42]


for number in numbers:
    count = 0
    number2 = number
    while number2 > 0 :
        
        number2 = number2 // 10
        count += 1
    
    print(number,"는",count,"자릿수입니다")