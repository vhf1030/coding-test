def solution(n, times):
    low = 0
    high = n * min(times)
    while low != high:
        mid = (low + high) // 2
        avail = sum(map(lambda x: mid // x, times))
        if avail >= n:
            high = mid
        else:
            low = mid + 1
    return low