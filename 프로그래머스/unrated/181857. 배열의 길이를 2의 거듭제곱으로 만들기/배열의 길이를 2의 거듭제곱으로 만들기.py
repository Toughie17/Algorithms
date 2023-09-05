def solution(arr):
    current = len(arr)
    two = 1
    
    while two < current:
        two *= 2
    
    if current != two:
        while len(arr) < two:
            arr.append(0)
            
    return arr
