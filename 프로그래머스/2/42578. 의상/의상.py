def solution(clothes):
    clothes_count_dict = {}
    for _, c in clothes:
        clothes_count_dict[c] = clothes_count_dict.get(c, 0) + 1
        # ccnt = clothes_count_dict.get(c)
        # if ccnt:
        #     clothes_count_dict[c] += 1
        # else:
        #     clothes_count_dict[c] = 1
    answer = 1
    for c in clothes_count_dict:
        answer *= (clothes_count_dict[c] + 1)
    return answer - 1
