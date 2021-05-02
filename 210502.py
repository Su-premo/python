print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1

print(abs(-5)) # absolute 절대값
print(pow(4,2)) # power 4^2 4의 2승.
print(round(3.14)) #반올림 3

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근 구하기. 4

from random import *
print(random()) # o.o이상 1.0미만의 임의의 값 생성
print(random() * 10) 
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(randrange(1,45)) # 1 ~ 45 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성, (필요한 숫자만큼 복붙)
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다")

python = "Python is Amazing"
print(python.lower())
print(python.upper())

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:5]
print(my_str)