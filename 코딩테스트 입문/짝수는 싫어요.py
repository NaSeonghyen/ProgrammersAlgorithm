def solution(n):
    return [i for i in range(n+1) if i % 2 != 0]

# 다른 사람의 풀이
# 컴프리헨션 사용, range 성질 이용
# def solution(n):
#   return [i for i in range(1, n+1, 2)]