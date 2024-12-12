def solution(s):
    x = s
    conv_cnt = 0
    rmv_cnt = 0
    while x != "1":
        rmv_cnt += x.count("0")
        n = x.count("1")
        x = bin(n)[2:]
        conv_cnt += 1
    answer = [conv_cnt, rmv_cnt]
    return answer