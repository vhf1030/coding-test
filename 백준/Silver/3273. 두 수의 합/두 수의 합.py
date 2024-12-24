# import sys.stdin.readline

n = int(input().strip())
seq = list(map(int, input().strip().split()))
x = int(input().strip())

seq.sort()
cnt = 0
i, j = 0, n - 1
while i < j:
    tmp = seq[i] + seq[j]
    if tmp == x:
        cnt += 1
        i += 1
        j -= 1
    if tmp < x:
        i += 1
    if tmp > x:
        j -= 1
    
print(cnt)