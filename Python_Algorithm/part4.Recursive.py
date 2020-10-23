def solution(x):
    
    """answer = 0
    count = 0
    f0 = 0
    f1 = 1
    f2 = f0 + f1

    while count < x:
        
        f0 = f1
        f1 = f2
        answer = f0
        f2 = f0 + f1
    
        
        count = count+1

    return answer"""

    """if x == 0 or x == 1:
        return x
    else :
        return solution(x-1) + solution(x-2)  """

    answer = 0
    num1 = 1
    num2 = 2
    
    if x>=2:
        for i in range(x):
            answer = num1 + num2
            num1 = num2
            num2 = answer
            i+1
        return num1
    else :
        return x

print(solution(3))

