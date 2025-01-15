n, k = map(int, input().split())
arr = list(map(int, input().split()))

def solution():
    cnt = 0
    for i in range(n):
        last = n - i - 1
        if last == 0:
            print(-1)
            return
        s = max(arr[:last])
        if s > arr[last]:
            curr = arr.index(s)
            arr[curr], arr[last] = arr[last], arr[curr]
            cnt += 1
            if cnt == k:
                print(' '.join([str(a) for a in arr]))
                return
            
solution()

