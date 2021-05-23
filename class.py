# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쓸 수 있는데, 일반 모드 / 시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)


# 클래스는 붕어빵으로 비유를 함. 붕어빵틀은 하나, 붕어빵은 계속 만들어낼 수 있음. 
# 클래스 = 하나의 틀. 서로 연관이 있는 함수와 변수의 집합이라 이해할 수 있음.

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


# __init__함수
# marine3 = Unit("마린") 또는 marine3 = Unit("마린", 40) 같은 경우는
# 예를 들어 missing 2 required positional arguments: 'hp' and 'damage'처럼 뜨는데,
# __init__함수는 ()안의 self를 제외한 name, hp, damage를 충족시켜줘야 객체를 만들 수 있음