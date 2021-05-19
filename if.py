# weather = "비" # 비(if)/미세먼지(elif)/기타-맑아요 등등(else)
# if 조건:
#     실행 명령문

# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")


# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")


temp = int(input("기온은 어때요? ")) # 기온은 숫자여서, input은 문자열로 값을 받음 -> int로 감싸줌
# int로 감싸주면 사용자가 입력한 값을 정수형태로 바꿔서 temp란 변수에 저장하게 됨.
if 30 <= temp:
    print("너무 더워요, 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10: # 0 <= temp < 10로도 표현 가능
    print("외투를 챙기세요")
else:
    print("너무 추워요, 나가지 마세요")

