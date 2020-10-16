"""
python에서는 else if를 대신하는 elif라는 문법이 존재함
들여쓰기와 블럭이 중요한 python에서 if else를 계속 물고들어간다면
코드의 가독성이 떨어질 수 있기 때문에
elif라는 문법을 사용해 else와 if를 한 블럭에서 처리할 수 있다.

"""

# else if문을 elif로 만들기
mine = "가위"
yours = "바위"

if mine == yours:
    print("비김")
else:
    if mine == "가위":
        if yours == "보":
            print("이겼다")
        else:
            print("졌다")
    else:
        if mine == "바위":
            if yours == "가위":
                print("이겼다")
            else:
                print("졌다")
        else:
            if mine == "보":
                if yours == "바위":
                    print("이겼다")
                else:
                    print("졌다")

mine = "보"
yours = "바위"

if mine == yours:
    print("비김")
else:
    if mine == "가위":
        if yours == "보":
            print("이겼다")
        else:
            print("졌다")
    elif mine == "바위":
            if yours == "가위":
                print("이겼다")
            else:
                print("졌다")
    elif mine == "보":
            if yours == "바위":
                print("이겼다")
            else:
                print("졌다")