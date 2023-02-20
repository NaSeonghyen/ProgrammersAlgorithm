def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

# 다른 사람의 풀이
# 리스트 컴프리헨션 문법 사용
# def solution(numbers):
#     return [num*2 for num in numbers]