#p. 115 변수

pi = 3.14159265   #변수명 = 값

r=10   #변수명 =값
# r2   #초기값 없으면 NameError:
 
print(pi,r) #변수를 참조

print(2 * pi * r) #변수를 참조

number =100
number += 10
number -= 10
number *= 2
number /= 2
number %=3
number **= 3
number = "안녕하세요"
number +="!"
number +="!"
print(number)


#p.118 입력함수

input("인사말을 입력하세요>")
string = input("입력>")   # 입력받은값 변수에 저장

print(type(string) )      # 123 -> str, 안녕 -> str
#p.121 타입변환, str -> int /float
string_int = int(string)
string_float = float(string)
print(type(string_int), type(string_float))
# <class 'int'> <class 'float'>

string_str = str(string_int)
print(type(string_str)) #<class 'str'>


#p. 125 누적 예제
raw_input = input("inch 입력:")
inch = int(raw_input)
cm = inch*2.54
print(cm)