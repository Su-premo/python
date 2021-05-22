# pickle : 프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장하는 것

import pickle
profile_file = open("profile.pickle", "wb") # write binary
profile = {"이름":"명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()


import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()




# with
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
# 따로 Close로 닫을 필요 없이, with문을 빠져나오면서 종료됨


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")


with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())