L = [2, 3, 5, 6, 9, 11, 15]
x = 6

def solution(L, x):
    
    answer = -1
    lower = 0
    upper = len (L) -1
    
    while lower <= upper:
      
        middle = (upper + lower) // 2
         
        if L[middle] == x:
            answer = middle
            break; 
        elif L[middle] < x:
            lower = middle+1
        else :
            upper = middle-1
        
    return answer
