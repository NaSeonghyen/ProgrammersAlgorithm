def solution(my_string, n):
    answer = ''
    for c in my_string:
        answer += c * n
    return answer

# 다른 사람의 풀이
# def solution(my_string, n):
#     return ''.join(i*n for i in my_string)