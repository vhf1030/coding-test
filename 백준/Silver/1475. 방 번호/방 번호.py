N = input()
num_arr = [0] * 10
for n in range(10):
    num_arr[n] = N.count(str(n))

num_arr[6] = int((num_arr[6] + num_arr[9] - 0.1) // 2 + 1)
num_arr[9] = 0
print(max(num_arr))
