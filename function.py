from ast import get_source_segment


def open_account():
    print("새로운 계좌가 생성되었습니다.")
# 함수는 정의만 되고 호출하기 전까지 실행되지 않음

open_account() # 호출해서 실행됨



# 전달값과 반환값
# 입금
def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance + money))
    return balance + money

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)


# 출금
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: # 잔액이 출금액보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000) # 출금이 완료되지 않았습니다. 잔액은 1000 원입니다.
balance = withdraw(balance, 500) # 출금이 완료되었습니다. 잔액은 500 원입니다.

# 저녁에 출금
def withdraw_night(balance, money)
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))



# 기본값
def profile(name, age, main_lang):
    print("이름 : {0}/t나이: {1}/t주 사용 언어: {2} \
        .format(name, age, main_lang"))

profile("재석", 20, "파이썬")
profile("태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이: {1}\t주 사용 언어: {2} \
        .format(name, age, main_lang"))

profile(재석)
profile(태호)


# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="재석", main_lang=20, age="파이썬")
profile(main_lang="자바", age=25, name="태호")


# 가변 인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5)
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ") # 문장을 출력하고 나서 이어서 밑에 있는 문장을 출력함
    print(lang1, lang2, lang3, lang4, lang5)

profile("재석", 20, "Python", "Jave", "C", "C++", "C#")
profile("태호", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language)
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()

profile("재석", 20, "Python", "Jave", "C", "C++", "C#", "Javascript")
profile("태호", 25, "Kotlin", "Swift", "", "", "")


# 지역변수와 전역변수
# 지역변수: 함수 내에서만 쓸 수 있는 변수 / 전역변수: 프로그램내 모든 공간에서 부를 수 있는 변수
gun = 10

def checkpoint(soldiers): # 경계근무
    gun = 20 # 지역변수 gun(=20)
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
# 출력값= 전체 총:10/ [함수 내] 남은 총: 18/ 남은 총: 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun(=10) 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
# 출력값= 전체 총:10/ [함수 내] 남은 총: 8/ 남은 총: 8

def checkpoint_ret(gun, soldiers) # checkpoint_return임
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return get_source_segment

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
# 출력값= 전체 총:10/ [함수 내] 남은 총: 8/ 남은 총: 8