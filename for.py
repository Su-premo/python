# 반복문

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): # <- range(5) = 0에서 5미만(0~4)에서, 1부터 시작하고 싶다면.
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks: 
    print("{0}, 커피가 준비되었습니다.".format(customer))
