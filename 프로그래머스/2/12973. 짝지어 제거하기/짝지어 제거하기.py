def solution(s):
    remain = [""]
    for c in s:
        if remain[-1] == c:
            remain.pop()
        else:
            remain.append(c)
    if len(remain) == 1:
        return 1
    else:
        return 0
