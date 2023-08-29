def solution(myString, pat):
    # replaced1 = myString.replace("B", "C")
    # replaced2 = replaced1.replace("A", "B")
    # replaced3 = replaced2.replace("C", "A")
    # return int(pat in replaced3)
    # 위 방식은 문자열을 세 번이나 바꾸기 때문에 문자열의 길이에 비례해서 시간이 소요되는 문제가 있음.
    # 문자열이 큰 경우에 비효율적임
    
    # 문자열을 한 번만 스캔하는 방식
    transformed = ""
    
    for cha in myString:
        if cha == "A":
            transformed += "B"
        elif cha == "B":
            transformed += "A"
            
    return int(pat in transformed)