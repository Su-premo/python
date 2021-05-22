print("Python", "Java") # Python Java
print("Python" + "Java") # PythonJava

# seperate는 ""안의 것으로 하겠다.
print("Python", "Java", sep=",") # Python,Java
print("Python", "Java", sep=" vs ") # Python vs Java
print("Python", "Java", "Javascript", sep=" vs ") # Python vs Java vs Javascript

print("Python", "Java", sep=",", end="?") # end의 의미는 문장의 끝부분을 물음표로 바꿔달라.임
print("무엇이 더 재밌을까요?") # end로 인해 이 두줄이 한줄로 출력됨


import sys
print("Python", "Java", file=sys.stdout) # 표준출력
print("Python", "Java", file=sys.stderr) # 표준에러
# 출력값은 Python Java로 똑같이 나오지만 다름


# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
# 딕셔너리임. keys(subjects) and values(scores).
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    # subject: 왼쪽으로 정렬, 총 8칸의 공간을 만들어달라.
    # score: 오른쪽으로 정렬, 총 4칸의 공간을 만들어달라.


# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    # print("대기번호 : " + str(num))
    print("대기번호 : " + str(num).zfill(3)) # 3개 크기의 공간, 값이 없는 곳은 0(zero)으로 채워달라.


answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
# 보통 숫자로 출력할 때는 str으로 감싸줘야하는데, 감싸주지 않아도 잘 실행됨.

print(type(answer)) # 10 또는 '코딩'을 입력 - 출력값: <class 'str'>
answer = 10
print(type(answer)) # 출력값: <class 'int'>
# 한마디로, 사용자입력을 통해서 값을 받게되면 항상 문자열 형태로 저장됨.