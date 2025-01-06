class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        tmp = s[0]
        for c in s:
            score_tmp = abs(ord(c) - ord(tmp))
            score += score_tmp
            tmp = c
        return score