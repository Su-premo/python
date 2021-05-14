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