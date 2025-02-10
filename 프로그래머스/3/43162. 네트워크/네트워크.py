# def solution(n, computers):
#     # DFS
#     stack = []
#     answer = 0
#     unconnected = list(range(0, n))
#     while unconnected:
#         if not stack:
#             answer += 1
#             stack = [unconnected.pop()]
#         i = stack.pop()
#         for j in range(n):
#             if computers[i][j] and j in unconnected:
#                 unconnected.remove(j)
#                 stack.append(j)
#     return answer

from collections import deque
def solution(n, computers):
    # BFS
    deq = deque()
    answer = 0
    unconnected = list(range(0, n))
    while unconnected:
        if not deq:
            answer += 1
            deq.append(unconnected.pop())
        i = deq.popleft()
        for j in range(n):
            if computers[i][j] and j in unconnected:
                unconnected.remove(j)
                deq.append(j)
    return answer