# 출석번호 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students]
print(students)

# 학생 이름을 길이로 변환, 공백도 카운트함 - 8, 4, 10으로 출력됨
students = ["Iron man", "Thor", "I am Groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am Groot"]
students = [i.upper() for i in students]
print(students)