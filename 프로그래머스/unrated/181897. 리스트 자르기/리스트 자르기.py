def solution(n, slicer, num_list):
    a, b, c = slicer
    
    dics = {
        1: num_list[0: b + 1], 2: num_list[a:], 3: num_list[a: b+ 1], 4: num_list[a:b + 1:c]
    }
    
    if n in dics:
        return dics[n]