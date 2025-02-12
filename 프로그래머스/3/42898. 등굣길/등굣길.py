# def solution(m, n, puddles):
#     path = [0] * m
#     path[0] = 1
#     col = 1
#     while col <= n:
#         path[0] = path[0] if not [1, col] in puddles else 0
#         for row in range(1, m):
#             path[row] = (path[row - 1] + path[row]) % 1000000007 if not [row + 1, col] in puddles else 0
#         col += 1
#     return path[-1]


def solution(m, n, puddles):
    path_arr = [[0] * (m+1) for _ in range(n+1)]
    path_arr[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles or [i, j] == [1, 1]:
                continue
            path_arr[i][j] = (path_arr[i-1][j] + path_arr[i][j-1]) % 1000000007
            
    return path_arr[i][j]