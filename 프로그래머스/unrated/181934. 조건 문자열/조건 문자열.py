def solution(ineq, eq, n, m):
    if (ineq == '>' and eq == '=' and n >= m):
        return 1
    elif (ineq == '<' and eq == '=' and n <= m):
        return 1
    elif (ineq == '>' and eq == '!' and n > m):
        return 1
    elif (ineq == '<' and eq == '!' and n < m):
        return 1
    
    return 0