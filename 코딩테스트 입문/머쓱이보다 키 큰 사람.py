def solution(array, height):
    cnt = 0
    for n in array:
        if n > height:
            cnt += 1
    return cnt

# 상대방 풀이
# def solution(array, height):
#     array.append(height)

#     # array.sort()
#     # array.reverse()
#     # == array.sort(reverse=True)
#     array.sort(reverse=True)
#     return array.index(height)