def solution(n):
    ans = 0
    remain = n
    while remain != 0:
        if remain % 2 == 1:
            ans += 1
        remain //= 2
    return ans