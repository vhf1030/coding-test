def solution(schedules, timelogs, startday):
    answer = len(schedules)
    for s, tl in zip(schedules, timelogs):
        late_time = s + 10 if s % 100 < 50 else s + 50
        today = startday % 7  # 토, 일 -> 6, 0
        for t in tl:
            if today == 6 or today == 0:
                today = (today + 1) % 7
                continue
            today = (today + 1) % 7
            if t > late_time:
                answer -= 1
                break
            
    return answer