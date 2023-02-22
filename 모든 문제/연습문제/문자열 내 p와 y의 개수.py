def solution(s):
    p_cnt,y_cnt = 0,0
    for i in s:
        if i == 'p' or i == 'P':
            p_cnt += 1
        if i == 'y' or i == 'Y':
            y_cnt += 1
    return p_cnt == y_cnt
    
    # 다른 사람의 풀이
    # return s.lower().count('p') == s.lower().count('y')
