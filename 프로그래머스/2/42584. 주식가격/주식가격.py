def solution(prices):
    answer = [0]  # 마지막 정답은 항상 0
    stack = []  # 떨어진 가격, 떨어지는데 걸린 시간
    for p in prices[-2::-1]:  # prices[-2::-1] == prices[:-1][::-1]
        t = 1
        while stack:
            p_tmp, t_tmp = stack.pop()  # (가장 최근의) 떨어진 가격, 떨어지는데 걸린 시간
            if p <= p_tmp:  # 가격이 떨어지지 않은 경우 - 기존의 떨어진 가격 및 시간 정보 제거
                t += t_tmp  # 가격이 떨어지는데 걸린 시간 추가
            else:  # 가격이 떨어진 경우
                stack.append((p_tmp, t_tmp))  # 떨어진 가격 및 시간 정보 다시 저장
                break
            
        stack.append((p, t))  # 현재 가격과 떨어지는데 걸린 시간 저장
        # print(p, t, stack)
        answer.append(t)
        
    answer.reverse()
    return answer
# 깃허브 제출용