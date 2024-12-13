def solution(n):
    answer = 1  # 자기 자신
    for i in range(1, n):
        start = i
        sum_tmp = start
        for j in range(start + 1, n):
            sum_tmp += j
            if sum_tmp == n:
                answer += 1
                break
            if sum_tmp > n:
                break
    return answer