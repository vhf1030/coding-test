def solution(want, number, discount):
    want_dict = {w: n for w, n in zip(want, number)}
    tmp = discount[:10]
    tmp_dict = {w: tmp.count(w) for w in want_dict}
    
    answer = 0
    if want_dict == tmp_dict:
        answer += 1
    
    for i in range(10, len(discount)):
        if discount[i-10] in tmp_dict:
            tmp_dict[discount[i-10]] -= 1
        if discount[i] in tmp_dict:
            tmp_dict[discount[i]] += 1
        if want_dict == tmp_dict:
            answer += 1

    return answer