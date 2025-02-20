from itertools import combinations

def solution(n, q, ans):
    answer = 0
    for c in combinations(range(1, n+1), 5):
        answer += 1
        a_set = set(c)
        for q_tmp, a_tmp in zip(q, ans):
            if len(a_set & set(q_tmp)) != a_tmp:
                answer -= 1
                break

    return answer