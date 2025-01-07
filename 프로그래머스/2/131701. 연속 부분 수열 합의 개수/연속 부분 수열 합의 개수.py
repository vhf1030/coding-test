def solution(elements):
    n = len(elements)
    pre_sum_set = set()
    round_elements = elements * 2
    for start in range(n):
        for size in range(1, n+1):
            pre_sum_set.add(sum(round_elements[start:start+size]))
    
    return len(pre_sum_set)