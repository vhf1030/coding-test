def solution(s):
    list_left = list(s)
    list_right = []
    while list_left:
        # print(list_left, list_right)
        list_right.append(list_left.pop())
        if len(list_right) < 2:
            continue
        if list_right[-1] == list_right[-2]:
            list_right.pop()
            list_right.pop()
        if not list_left and not list_right:
            return 1
    return 0