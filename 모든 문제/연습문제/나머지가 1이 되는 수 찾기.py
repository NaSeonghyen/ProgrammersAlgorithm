def solution(n):
    arr = []
    for i in range(1,n):
        if n % i == 1:
            arr.append(i)
        else:
            continue
    return arr[0]