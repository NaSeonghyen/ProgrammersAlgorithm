def solution(s1, s2):
    cnt = 0

    for i in s1:
        for j in s2 :
            if i == j:
                cnt += 1
    return cnt
# 다른 사람의 풀이
# 집합 {} 성질 이용
# def solution(s1, s2):
#     return len(set(s1)&set(s2));