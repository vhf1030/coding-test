N = input()
num_dict = dict()
for _ in range(0, 10):
    n = str(_)
    num_dict[n] = N.count(n)
    # print(n, ':', N.count(n))
num_dict['6'] = int((num_dict['6'] + num_dict['9'] - 0.1) // 2) + 1
num_dict['9'] = 0

print(max(num_dict.values()))