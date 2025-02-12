def solution(m, n, puddles):
    path = [0] * m
    path[0] = 1
    col = 1
    while col <= n:
        path[0] = path[0] if not [1, col] in puddles else 0
        for row in range(1, m):
            path[row] = (path[row - 1] + path[row]) % 1000000007 if not [row + 1, col] in puddles else 0
        col += 1
    return path[-1]