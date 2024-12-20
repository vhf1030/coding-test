def solution(k, tangerine):
    answer = 0
    size_cnt_dict = dict()
    for t in tangerine:
        if t not in size_cnt_dict:
            size_cnt_dict[t] = 0
        size_cnt_dict[t] += 1
    size_cnt = sorted(size_cnt_dict.values(), reverse=True)
    
    current = 0
    for s in size_cnt:
        answer += 1
        current += s
        if current >= k:
            return answer
    return answer