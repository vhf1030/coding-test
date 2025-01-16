# def solution(numbers):
#     str_numbers = [str(n) for n in numbers]
#     # def str_sort(s):
#     #     while len(s) < 4:
#     #         s += s
#     #     return s[:4]
#     # str_numbers.sort(key=str_sort, reverse=True)
#     str_numbers.sort(key=lambda s: s*3, reverse = True)
#     return str(int(''.join(str_numbers)))

def str_compare(s1, s2):
    # s1이 s2보다 크니?
    n, m = len(s1), len(s2)
    i = 0
    while i < 4:
        t1 = s1[i % n]
        t2 = s2[i % m]
        if t1 > t2:
            return True
        if t1 < t2:
            return False
        i += 1
    return False  # 서로 같은 경우
    
    
def str_merge_sort(str_list):
    if len(str_list) == 1:
        return str_list
    mid = len(str_list) // 2
    arrA = str_merge_sort(str_list[:mid])
    arrB = str_merge_sort(str_list[mid:])
    result = []
    while arrA and arrB:
        if str_compare(arrA[0], arrB[0]):  # arrA[0]이 더 큰 경우
            result.append(arrA.pop(0))
        else:
            result.append(arrB.pop(0))
    result += arrA + arrB  # 남은애가 있으면 넣어주기
    return result

def solution(numbers):
    str_numbers = [str(n) for n in numbers]
    answer = str_merge_sort(str_numbers)
    if answer[0] == "0":
        return "0"
    return ''.join(answer)

