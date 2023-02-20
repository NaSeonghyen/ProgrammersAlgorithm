def solution(numbers):
    numbers.sort()
    first_max = numbers.pop()
    second_max = numbers.pop()
    return first_max * second_max

# 리스트 정렬, 스택 특징 사용(pop)

# 다른 사람의 풀이
# def solution(numbers):
#     numbers.sort()
#     return numbers[-2] * numbers[-1]

# 원리는 비슷한데 리스트 인덱스 사용하여 해결함.