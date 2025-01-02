# _ = int(input().strip())
_ = input()
n_set = set(map(int, input().strip().split()))
# _ = int(input().strip())
_ = input()
m_list = list(map(int, input().strip().split()))

for m in m_list:
    if n_set & {m}:
        print(1)
    else:
        print(0)

