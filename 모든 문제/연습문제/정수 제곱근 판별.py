def solution(n):
    return (int(n**(1/2))+1) ** 2 if n == int(n**(1/2)) * int(n**(1/2)) else -1
    