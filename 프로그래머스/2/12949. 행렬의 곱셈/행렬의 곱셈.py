def solution(arr1, arr2):
    # print(list(zip(*arr2)))
    # print(list(zip(arr1, zip(*arr2))))
    answer = [[0] * len(arr2) for _ in range(len(arr1))]
    print(answer)
    arr2_t = zip(*arr2)
    for a1, a2t in zip(arr1, arr2_t):
        print(a1, a2t)
    return answer