score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 항상 닫아주는 걸 잊으면 안됨
# 파일이 생성됨.


score_file = open("score.txt", "a", encoding="utf8")
# 내용이 존재하는 파일에 이어서 쓰고 싶다면
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # print때는 줄이 저절로 바뀌지만, write는 줄바뀜이 없으므로 


# 파일에 있는 내용을 한번에 불러오는 것
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()


score_file = open("score.txt", "a", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline()) 
print(score_file.readline())
print(score_file.readline())
score_file.close()
# print는 저절로 줄바꿈을 하기 때문에, 한 줄 띄고 출력됨. 원하지 않는다면
score_file = open("score.txt", "a", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()


# 파일이 몇줄인지 모를 때 반복문(while)을 통해서 파일의 내용을 불러올 수 있음
score_file = open("score.txt", "r", encoding="utf8") # r은 읽기모드
while True:
    line = score_file.readline()
    if not line:
        break # 반복문 탈출
    print(line) # 줄바꿈하지 않으려면 print(line, end""")
score_file.close()


# 값을 다 리스트에 넣어서 처리하기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()
# 파일에 있는 모든 내용을 모든 줄을 가지고 와서 리스트형태로 집어넣고, 리스트에서 한줄씩 불러와서 출력해주는 역할