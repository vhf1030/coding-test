def solution(triangle):
    triangle.reverse()
    while triangle:
        t0 = triangle.pop()
        if not triangle:
            return max(t0)
        t1 = triangle.pop()
        mid = []
        for i in range(1, len(t1) - 1):
            t0_max = max(t0[i-1], t0[i])
            mid.append(t0_max + t1[i])
        triangle.append([t0[0] + t1[0]] + mid + [t0[-1] + t1[-1]])
    return answer