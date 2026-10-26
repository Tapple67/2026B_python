# 비교연산자
 #==,!=, >, < , >= ,<=
#p.158
x=25
print(10 < x < 30)
#논리 연산자# not, and, or
print( not True)
print( True and True)
print( True and False)
print( True or False)

#p.163 , if 조건문

# if 조건식:
#     (tab 들여쓰기)참이면
age =10
if age>=19:
    print('성인입니다')
# if~ else
# if 조건식 :
#   (tab들여쓰기)참이면
# else : 
#   (tab들여쓰기)거짓

number = 13 
if number %2 ==0:
    print('짝수')
else :
    print("홀수")

#if ~ elif ~ elif ~

point = 85
if point >= 90 :
    print('A')
elif point >=80:
    print('B')
elif point >= 70:
    print('c')
else:
    print('재시험')

# 중첩if
x=10;
if x>5:
    if x > 10 : 
        print('10보다크다')
    else :
        print('5보다크고 10보다 작다')
else:
    print('5보다 작다')


x=10
y=2
if x >4:
    if y > 2:
        print(x*y)
else:
    print(x+y)


    
x=2
y=10
if x >4:
    if y > 2:
        print(x*y)
else:
    print(x+y)

x=12
if 10 <x<20:
    print("ㅇㅇ")


a = input("dd>")
b = int(a)%12

if b ==0:
    print('원숭')
elif b ==6:
    print('범')