def solution(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(sum)
    return sum
# 다른 사람의 풀이
# 리스트 컴프리헨션 사용
    # return sum(int(i) for i in str(n))