def solution(arr):
    x = 0
    
    while True:
        current = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                current.append(num // 2)
            elif num < 50 and num % 2 == 1:
                current.append(num * 2 + 1)
            else:
                current.append(num)
        
        if arr == current:
            break
        arr = current
        x += 1
        
    return x
        