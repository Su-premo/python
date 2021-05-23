# 상속
# 유닛과 어택유닛에서 겹치는 부분이 있음. self.name이나 self.hp
# 유닛이라는 클래스의 내용을 상속받아 어택유닛을 만들기(부모-자식같은 관계)
# method 필기와 함께 볼 것

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location): # 클래스 내에서 메소드 앞은 항상 self를 적어줌.
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # location은 전달받은 값을 쓴다는 것(self를 붙이지 않았음)

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 다중상속. 부모가 둘 인 것 같은, 여러곳에서 상속받는 것.

# 드랍쉽: 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송하여 다른 곳에 떨어트려 줌. 공격기능은 없음.

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속은 콤마로 구분하면 됨
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사. 강력한 유닛
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")