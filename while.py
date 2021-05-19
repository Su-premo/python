# while은 조건이 만족할 때까지 반복하라는 것

# 다섯번 불렀는데 나타나지 않으면 커피를 버리는 정책
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1 # index를 한번씩 줄여나감
    if index == 0: # index가 0이 된다면
        print("커피는 폐기처분되었습니다.")

# 계속반복, 무한루프에 빠짐
# ctrl C를 누르면 강졔종료가 됨
customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1 

# 손님 호명?
customer = "토르"
person = "Unknown"

while person != customer : # person이 내가 원하는 customer가 아닐 때
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ") # person이라는 변수에 이름을 묻는 input을 썼음
    # print를 하면 토르, 커피가 준비되었습니다. 이름이 어떻게 되세요?라고 물어봄.
    # 다른이가 오면 다시 외침, 토르가 온다면 while문을 탈출하게 됨.