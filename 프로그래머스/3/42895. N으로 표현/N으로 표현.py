def calculate(a, b):
    result = {a + b, a - b, a * b}
    if b and not a % b:
        result.update([a // b])
    return result

def solution(N, number):
    if N == number:
        return 1
    count = 1
    result_dict = {1: {N}}
    while count <= 8:
        count += 1
        join_N = int(str(N) * count)
        result_dict[count] = {join_N}
        for c in range(1, count):
            for i in result_dict[c]:
                for j in result_dict[count - c]:
                    result = calculate(i, j)
                    result_dict[count].update(result)
        if number in result_dict[count]:
            return count
    return -1