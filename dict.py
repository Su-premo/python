cabinet = {3:"재석", 100:"태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# 프로그램 종료됨, 오류. 5라는 키가 없기 때문.
print(cabinet[5])
print("hi") 

# none, hi가 출력됨. none을 출력하고 이어나감.
print(cabinet.get(5))
print("hi")

# none, 사용 가능, hi
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False


cabinet = {"A-3":"재석", "B-100":"태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님, 값을 업데이트하거나 추가.
print(cabinet)
cabinet["A-3"] = "종국"
cabinet["C-20"] = "세호"
print(cabinet)

# 떠난 손님, 키 삭제.
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# Key, value 쌍으로 출력
print(cabinet.items())

# 폐점, 손님들이 다 떠남, 빈 중괄호가 출력됨.
cabinet.clear()
print(cabinet)