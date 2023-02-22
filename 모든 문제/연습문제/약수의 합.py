def solution(n):
    sum = 0
    if   n == 0:
        return 0
    else:
        for i in range(n):
            i += 1
            if n % i == 0:
                sum += i
        return sum
# 다른 사람의 풀이
# n/2 약수 + n을 하면 확실히 성능은 2배 좋아 질 것 같다.(n/2 ~ n 까지를 탐색하지 않아도 되기 때문임.)
# 리스트 컴프리헨션 사용
    # return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])