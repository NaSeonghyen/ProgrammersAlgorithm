def solution(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum

# 다른 사람의 풀이
# divmod 함수 사용, while 0인 경우 false 이용
# def solution(n):
#     answer = 0
#     while n:
#         n, r = divmod(n, 10)
#         answer += r
#     return answer