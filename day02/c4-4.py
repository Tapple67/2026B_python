# p. 251
numbers = [103, 52, 273, 32, 77]

print( min(numbers ) ) #min( 리스트) 최솟값
print( max(numbers ) ) #max( 리스트) 최댓값
print( sum(numbers ) ) #sum( 리스트) 합계


#p.252 revered
numbers_revered = reversed(numbers) # 리스트 뒤집기
print (list(numbers_revered))

# int() folat() str() list() : 특정 타입으로 변환 함수

# 이터러블 : 요소들을 하나씩 차례로 꺼내기 가능한 객체 의미
# 이터레이터 이터러블 중에서 하나씩 차례로 꺼낼 수 있는 요소
# 이터레이터 가능한 타입 : 리스트 / 딕셔너리/ 문자열/ 튜플
# 이터레이터 하나씩 꺼내는 함수 = next() 함수 ---> 이터러블

#p.254 enumerate
numbers = [103, 52, 273,32,77]
print(enumerate(numbers))
print(list(enumerate(numbers))) # [(0, 103),(1, 52),(2, 273), (3, 32),(4, 52)]

for index, value in enumerate(numbers):
    print( index, value)

#p. 256 items(딕셔너리).items(), [(key,value), (key,value)]
dict_a = {"name": "유재석","age" :10}
for key , value in dict_a.items():
    print(key,value)

#p. 258 리스트 내포 , 인덱스 자리에 반복문 사용 가능
# 0 부터 20까지 2씩 증가한 자료들을 리스트에 저장
# 방법1]
array = []
for i in range(0, 21, 2):
    array.append(i)

# 방법2] 리스트 변수 = [값 for 반복변수 in range()]
array = [ i for i in range(0, 21, 2)]
print(array)

#활용 : 10 제외한 , 리스트변수 = [값 for 반복변수 in range() if 조건식 ]
array = [ i for i in range(0, 21, 2) if i != 10]
print(array)

#p. 263 , .join()
#방법1] """여러줄 """
print("""안녕하세요1
안녕하세요2""")

#방법2] \n 제어문자

print("안녕하세요1\n안녕하세요")

#방법3] ("문자열" "문자열" "문자열") # 튜플 차이
print(("안녕하세요1\n" "안녕하세요2"))

#방법4]
print("\n".join(["안녕하세요1" , "안녕하세요2"]))
print("-".join("유재석"))

pets = [
    {"name": "구름", "age":5},
    {"name": "초코", "age":3}
]

for x in pets:
    print (x.get('name'), str(x.get('age')) + '살')


numbers = [1,2,6,8,4,3,2,1,2,3,4,5]
counter = {}

for number in numbers:
    if  number not in counter:
        counter[number] = 1
    else:
        counter[number] += 1
print(counter)

key_list = ["name", "hp"]
value_list = ["기사",200]
character ={}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)

limit = 10000
i = 1
sum_value = 0
while True:
    sum_value += i
    i += 1

    if(sum_value > limit):
        break

print(sum_value)

max_value = 0
a=0
b=0

for i in range(1,100):
    j  = 100 - i

    if i * j > max_value:
        max_value = i*j

print(max_value)

output = [x for x in range(1,101) if ("{:b}".format(x)).count("0") == 1 ]


for i in output:
    print("{}:{}".format(i,"{:b}".format(i)))
print("합계:",sum(output))
