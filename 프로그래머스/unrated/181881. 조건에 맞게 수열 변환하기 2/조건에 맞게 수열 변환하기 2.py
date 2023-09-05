def solution(arr):
    x = 0
    
    while True:
        new = []
        for num in arr:
            if num >=50 and num % 2 == 0:
                new.append(num // 2)
            elif num < 50 and num % 2 == 1:
                new.append(num * 2 + 1)
            else:
                new.append(num)
        if arr == new:
            break
        else:
            arr = new
            x += 1
            
    return x