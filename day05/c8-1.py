#절차지향 프로그래밍: 데이터를 순서대로 처리하고 하향식 순차 실행 흐름, C
#객체지향 프로그래밍 : 객체들의 상호작용으로 프로그래밍 생각해서 프로그래밍 , JAVA/PYTHON/JS
#관점지향 프로그래밍 : 공통되는 기능(로그/검증/보안 등) 들을 분리하여 프로그래밍 설계, 스프링

# 추상화 : 핵심적인 개념 또는 기능 간추려 내는 것
# [리스트], {딕셔너리} 객체이다.
# 클래스: 추상화한 데이터들을 구조화 한것 ( 설계도 )
# 객체 : 세상에 존재하는 모든 데이터들을 추상화 (실체X) -> 개념적 객체
#인스턴스: 추상화한것을 객체 만든것 ( 실체 O ) -> 물리적 객체
# 생성자: 클래스 기반으로 인스턴스 만드는 함수 -> 인스턴스 초기화 함수

#1. 클래스 만들기
# class 클래스 명:
class Student :
    pass
student = Student() #JAVA : new Student(), PY: Student()
students = [
            Student(),
            Student(),
            Student(),
            Student(),
            Student(),
            Student(),
            Student(),
            Student(),
            Student()
            ]

#2. 생성자, 메소드
class Student:
    def __init__(self,멤버변수1, 멤버변수2, 멤버변수3):
        self.멤버변수1 = 멤버변수1

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + \
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

#일반함수 와 메소드 차이? 일반함수는 클래스 밖에서 독립 선언 / 메소드는 클래스 안에서 내부선언
# 일반함수에서는 self 없고 메소드는 self 있다.
def get_sum2():
    pass

# 생성자 이용한 인스턴스 생성
# Student2 s =new Student("유재석", 10, 20, 30, 40)
students = [
    Student("윤인성", 87, 98, 88, 85),
    Student("윤인성", 87, 98, 88, 85),
    Student("윤인성", 87, 98, 88, 85),
    Student("윤인성", 87, 98, 88, 85),
    Student("윤인성", 87, 98, 88, 85),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())


#상속이란? 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스 만드는것
#isinstance(인스턴스, 클래스명)
#예1
class Student : 
    def __init__(self):
        pass
class Human:
    def __init__(self):
        pass

student = Student()

print (isinstance(student,Student)) # true
print (isinstance(student,Human)) # false

#예] 

class Student:
    def __init__(self,멤버변수1, 멤버변수2, 멤버변수3):
        self.멤버변수1 = 멤버변수1

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + \
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

#특수한 이름의 메소드
    def __str__(self):
        return "{}\t{}\t{}".format(\
                    self.name,\
                    self.get_sum(),\
                    self.get_average())

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
         

        
        
#일반함수 와 메소드 차이? 일반함수는 클래스 밖에서 독립 선언 / 메소드는 클래스 안에서 내부선언
# 일반함수에서는 self 없고 메소드는 self 있다.
def get_sum2():
    pass

# 생성자 이용한 인스턴스 생성
# Student2 s =new Student("유재석", 10, 20, 30, 40)
students = [
    Student("윤인성", 87, 98, 88, 85),
    Student("윤인성", 87, 98, 88, 85),
    Student("윤인성", 87, 98, 88, 85),
    Student("윤인성", 87, 98, 88, 85),
    Student("윤인성", 87, 98, 88, 85),
]

print("이름","총점","평균",sep="\t")
for student in students:
    print(str(students[0]))

print( str(students[0]) )  # __str__함수가 실행된다.

print(students[0]==students[1])
#원래 객체는 다른데 우리가 __eq__ 메소드에서 같다 기준을 총합계 정의 했으므로 # true
print(students[0] != students[1]) #
#원래 객체는 다른데. 우리가 __ne__ 메소드에서 다르다 기준을 총합계 정의 했으므로 #false
