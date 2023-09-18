def solution(bin1, bin2):
    sol = int(bin1,2) + int(bin2,2)
    return bin(sol)[2:]
#'0b1010'