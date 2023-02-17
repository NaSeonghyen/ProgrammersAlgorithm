def solution(strlist):
    list = []
    for i in strlist:
        list.append(len(i))
    return list

# 다른 사람의 풀이
# def solution(strlist):
#     answer = list(map(len, strlist))
#     return answer