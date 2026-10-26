#p.231
# 범위함수 : range()
#1. range( 수)
print (range (5)) #range(0,5)

print(list(range(5))) # [0,1,2,3,4]

#2. range(시작값, 끝값) #range( 2, 10) -> 2~9

print (list(range(3,6))) # [3,4,5]


#3. range0(시작값 , 끝값, 단계)
print(list (range(0,10,2))) # 0부터 9까지 2씩 증가

#p.233
# for 과 range 함수 함께 , for 반복변수 in range() :
    # 1] 1부터 10까지 출력
for i in range(1,11):
    print(i)

    #2] 10부터 1까지 출력
for i in range ( 10, 0, -1 ):
    print(i)

    #3] 1부터 10까지 홀수만 출력
for i in range(1, 11, 2) :
    print(i)

#4] 구구딘 : 단수 2부터 9까지
for 단 in range(2,10,1):
    for 곱 in range(1, 10,1) :
        print(단* 곱)

i = 1
while i <11:
    print(i)
    i+=1

# 예2] while과 리스트
list_a = [1,2,1,2]
value = 2
while value in list_a:
    #리스트내 2가 존재하면 반복실행
    list_a.remove(value)
print(list_a)

#p.244 break, continue 키워드
for i in range(1, 11, 1):
    print(i)
    # 만약에 i가 3이면 반복문 종료/즉] break 아래 부분 실행 안됨
    if i == 3:
        break  # 코드의 흐름이 break 만나면 가장 가까운 반복문 탈출/종료

for i in range(1, 11, 1):
    if i == 3:
        # 만약에 i가 3이면 반복문으로 이동/즉] 아래 부분 실행 안됨
        continue #코드의흐름이 continue 만나면 가장 가까운 반복문으로 이동
    print(i)
    