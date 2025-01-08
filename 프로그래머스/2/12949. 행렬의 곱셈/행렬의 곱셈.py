def solution(arr1, arr2):
    answer = []
    arr2_t = list(zip(*arr2))
    for a1 in arr1:
        row = []
        for a2t in arr2_t:
            row.append(sum([x * y for x, y in zip(a1, a2t)]))
        answer.append(row)
    return answer