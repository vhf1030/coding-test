
_ = input()
n_list = list(map(int, input().strip().split()))

_ = input()
m_list = list(map(int, input().strip().split()))

n_dict = {}
for n in n_list:
    n_dict[n] = n_dict.get(n, 0) + 1
    
for m in m_list:
    print(n_dict.get(m, 0))