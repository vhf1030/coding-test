def solution(s):
    answer = ""
    for i, c in enumerate(s):
        if i == 0 or s[i-1] == " ":
            answer += c.upper()
        else:
            answer += c.lower()
    return answer