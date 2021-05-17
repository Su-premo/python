# Tuple
# 여러 개의 데이터를 하나로 묶는데 사용
# 그 값을 변경할 수 없음 (immutable type)

# 아무런 요소도 저장하고 있지 않는 빈 튜플(empty tuple)은 ()로 표현

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 'tuple' object has no attribute 'add'
menu.add("생선까스")

name = "종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("종국", 20, "코딩")
print(name, age, hobby)