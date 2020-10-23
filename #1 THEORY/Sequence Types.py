# 열거형 타입 (Sequence type) 
# 파이썬의 열거형 타입 두가지 : list, tuples (range 는 일단 예외로 치고)
# https://docs.python.org/ko/3/library/stdtypes.html#sequence-types-list-tuple-range

# List : list = [..., ..., ...]
# list는 공통과 가변 시퀀스 연산을 모두 구현가능함

days = ["월", "화", "수", "목", "금"]
days2 = [1, 2, 3, 4, 5, True, False]

#####################################################################################

# 공통(Commons) 연산: https://docs.python.org/ko/3/library/stdtypes.html#typesseq-common
# x in s / x not in s : list 내에 해당 원소가 존재하는 지/안하는 지
print("월" in days)
print("Monday" not in days)

# s + t : list를 합쳐줌
print(days+days)
print(days+days2) # 내부 데이터의 형태가 달라도 합칠 수 있음.. 개쩌네 ㄹㅇ루

# len(s) : list의 길이를 반환함
print(len(days2))

# 등등 많은 공통 연산이 존재함(유용한게 많아보이니 라이브러리 적극활용 필수일듯)

#####################################################################################

# 가변(Mutable) 연산: 값을 변경할 수 있는 시퀀스
# 값을 변경하고 싶지 않다면 Immutable 시퀀스를 사용해야함 (list는 Mutable 시퀀스)
# https://docs.python.org/ko/3/library/stdtypes.html#typesseq-mutable

# s.append(x) : list에 원소를 추가함
days.append("토")
print(days)

# s.reverse() : list의 원소를 역순으로 정렬함
days.reverse()
print(days)

# 여기도 유용한게 많아보이니 라이브러리를 적극 활용해서 한번 찾아보자

###################################################################################

# Tuple : tuple = (..., ..., ...)
# Tuple은 불가변(Immutation) 시퀀스이므로 공통 연산만 할 수 있음

t_days = ("월", "화", "수", "목", "금")
#t_days.append("토") = 불가능
print(len(t_days)) # = 가능

###################################################################################

# Dictionary : dictionary = {"a":..., "b":..., "c":...}

KSY = {
    "name": "김승연", 
    "age": 29, 
    "nationality": "대한민국", 
    "fav_food": ["고기", "치킨"]
    }

print(KSY)
KSY["hobby"] = "게임"
print(KSY)
