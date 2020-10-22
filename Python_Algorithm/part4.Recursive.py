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

    if x == 0 or x == 1:
        return x
    else :
        return solution(x-1) + solution(x-2)    
    
    

x = 50
print(solution(x))

