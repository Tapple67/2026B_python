
class Student:

    count = 0

    @classmethod # 클래스함수 정의 하는 데코레이터/어노테이션
    def print(cls) : # 매개변수에 cls 관례적으로 선언
        for student in cls.students : # cls.클래스 변수 vs student2.클래스변수
            print( str(student))
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