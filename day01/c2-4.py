#p.135 , "문자열".format(값)

string_a = "age:{}".format(10)
print(string_a) # age:10
string_b = "{} {} {}".format(1,"안녕",True)
print(string_b)
# 주의 할점: {}개수와 값의 개수는 일치해야한다.

# p.137~ p.140 생략
# p.141, 대소문자

a="Hello"

print(a.upper()) # HELLO

print(a.lower()) # hello

#p.142, 양쪽 여백 /공백 제거

a = " hello python "
print(a.strip())

#p. 143 , isOOO 구성 확인, 반환 타입, True/False
print("HELLO".isalpha())

print("HELLO".isdigit())

# p.144 , find() vs indexOf()

output_a = "안녕안녕하세요".find("안녕")
print(output_a) #0 : 인덱스
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

output_c = "안녕안녕하세요".find("hello")
print(output_c)

#p.145 , 찾을 값 in 문자열 , 없으면 False 있으면 True 
print("안녕" in "안녕하세요") # True 
print("hello" in "안녕하세요") # False

#p.145, "문자열".split(기준문자)
a="10 20 30 40 50".split(" ")
print(a) #리스트, ['10','20','30','40','50']
print(a[2]) #30 

num =10
#p.146 , f-문자열
a1= "{}".format( num )
a2= f"age:{ num }"
a3 = "age:num"