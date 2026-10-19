print(type("안녕하세요")) #<class 'str'>
print(type(123))          #<class 'int'>
print(type(1.23))         #<class 'float'>
print(type(True))         #<class 'bool'>
print(type(None))         #<class 'NoneType'>
print(type([]))           #<class 'list'>
print(type({}))           #<class 'dict'>
print(type(()))           #<class 'tuple'> 수정하지 못하는 집합

#86p. 문자열 만들기
print("ABC")
print('ABC')

print("""A
B
C""")           # """ 여러줄 """ 감싼 
print("A'b'c")  #작은 따옴표 출력
print('A"B"C')
print("\"A\'B\nC\tD\\E")