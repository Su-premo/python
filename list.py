# 리스트 [ ]

subway = [10, 20, 30]
print(subway)

subway = ["재석", "세호", "명수"]

# 세호가 몇 번째 칸에 타고 있는가?
print(subway.index("세호")) 

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 형돈이를 재석과 세호 사이에 태우기
subway.insert(1, "형돈")
print(subway)

# 지하철에 있는 사람들 한 명씩 뒤에서 꺼내기(세 명을 보내려면 3번 반복)
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("재석")
print(subway)
print(subway.count("재석"))

# 정렬
num_list = [5,2,3,1,4]
num_list.sort()
print(num_list)

# 정렬 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
# True라고 대문자로 시작해서 써야하는 듯
mix_list = ["세호", 21, True]
print(mix_list)

# 리스트 확장
num_list = [5,2,3,1,4]
mix_list = ["세호", 21, True]
num_list.extend(mix_list)
print(num_list)