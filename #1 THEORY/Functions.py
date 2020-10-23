# Built in Function (내장함수)
# https://docs.python.org/ko/3/library/functions.html
# 파이썬 내부에 이미 제공되어 있는 함수

# Define Funciont (함수 만들기)

def say_hello():
    print("안녕?") # 들여쓰기 주의

say_hello()

# argument : 인자

def say_hello2(who): # who = 인자
    print("안녕?, "+who)

say_hello2("파이썬")

def calculator(a, b):
    print(a + b)
    print(a - b)
    print(a*b)
    print(a/b)
    print(a%b)
    print(a//b)

calculator(7, 5)

# default Value : 인자에 값을 지정해 줄 수 있음

def say_hello3(who="월드"): # who = 인자
    print("안녕?, "+who)

say_hello3()

def calculator2(a, b=50):
    print(a + b)
    print(a - b)
    print(a*b)
    print(a/b)
    print(a%b)
    print(a//b)

calculator2(800)