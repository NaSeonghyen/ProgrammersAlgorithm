def solution(n):
    arr = []
    while n:
        arr.append(n % 10) 
        n = n // 10
    return arr

# 다른 사람의 풀이
# def solution(n):
#     return list(map(int, reversed(str(n))))
