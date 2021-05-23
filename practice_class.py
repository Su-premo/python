class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): # 다중상속 + super : 순서상 맨처음에 상속받는 클래스에 대해서만 Init함수가 호출이 됨
    def __init__(self):
        super().__init__()
        # 출력값: Flyable 생성자
 #class FlyableUnit(Flyable, Unit): # 두번을 통해서 초기화하는 방식
 #   def __init__(self):       
 #       Unit.__init__(self)
 #       Flyable.__init__(self)
        # 출력값: Unit 생성자 
        #        Flyable 생성자
 

# 드랍쉽
dropship = FlyableUnit()