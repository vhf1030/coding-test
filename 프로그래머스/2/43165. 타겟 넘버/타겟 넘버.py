# from itertools import product
# def solution(numbers, target):
#     n_all = [(-n, n) for n in numbers]
#     sum_all = [sum(p) for p in product(*n_all)]
#     # sum_all = list(map(sum, product(*n_all)))
#     return sum_all.count(target)


def solution(numbers, target):
    # dfs
    n = len(numbers)
    answer = 0
    
    val = numbers[0]
    step = 1
    stack = [(val, step), (-val, step)]
    while stack:
        val, step = stack.pop()
        if step == n:
            if val == target:
                answer += 1
            continue
        
        stack += [
            (val + numbers[step], step + 1),
            (val - numbers[step], step + 1)
        ]
    
    return answer
        
        
        
        
        
