# 선생님이 책을 읽게하는데 결석한 친구들은 넘어가고 다른 친구들을 읽게 하는 게 continue
# continue는 아래 있는 문장을 더이상 실행시키지 않고 다음 반복으로 진행하도록 하라는 것

absent = [2, 5] # 결석
no_book = [7] # 책을 안가져온 학생
for student in range(1, 11): # 1에서 10번까지 출석번호가 있음(1,2,3,4,5,6,7,8,9,10)
    if student in absent: 
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# continue는 그 이후 문장을 실행하지않고 다음 반복으로 넘어가는 것
# break는 뒤에 반복값이 있음과 상관없이 반복문을 탈출하는 것