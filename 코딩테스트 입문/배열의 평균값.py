def solution(numbers):
    # 첫번째 풀이
    sum = 0
    for i in numbers:
        sum += i
    return sum/len(numbers)
    
    # 두번째 풀이(참고)
    # import numpy as np
    # return np.mean(numbers)