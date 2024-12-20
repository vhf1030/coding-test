def solution(prices):
    answer = [0]
    stack = [(prices.pop(), 0)]  # 마지막 가격, 시간
    prices.reverse()
    for p in prices:  # for문이 좀더 빠름
    # while prices:
    #     p = prices.pop()
        sec = 1
        while stack:
            s = stack.pop()  # 마지막 가격이 더 높은 경우 저장하지 않음
            if p > s[0]:
                stack.append(s)  # 마지막 가격이 더 낮은 경우만 저장함
                break
            sec += s[1]  # 현재 가격에 시간 업데이트
        stack.append((p, sec))  # 현재 가격 정보를 마지막 가격으로 옮김
        answer.append(sec)
    answer.reverse()
    return answer