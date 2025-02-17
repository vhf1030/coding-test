# def calculate(a, b):
#     result = {a + b, a - b, a * b}
#     if b and not a % b:
#         result.update([a // b])
#     return result

# def solution(N, number):
#     if N == number:
#         return 1
#     count = 1
#     result_dict = {1: {N}}
#     while count <= 8:
#         count += 1
#         join_N = int(str(N) * count)
#         result_dict[count] = {join_N}
#         for c in range(1, count):
#             for i in result_dict[c]:
#                 for j in result_dict[count - c]:
#                     result = calculate(i, j)
#                     result_dict[count].update(result)
#         if number in result_dict[count]:
#             return count
#     return -1


def solution(N, number):
    result_dict = {cnt: set([int(str(N)*cnt)]) for cnt in range(1, 9)}
    # print(result_dict)
    for cnt in range(1, 8):
        if number in result_dict[cnt]:
            return cnt
        
        idx_tuple = [(c, cnt+1 - c) for c in range(1, cnt+1)]
        for i1, i2 in idx_tuple:
            for r1 in result_dict[i1]:
                for r2 in result_dict[i2]:
                    res_set = {r1 + r2, r1 - r2, r1 * r2, r1 // r2} - {0}
                    result_dict[cnt+1].update(res_set)
                    
    if number in result_dict[8]:
        return 8
    
    return -1
