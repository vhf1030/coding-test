N = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

def solution(N, arrA, arrB):
    
    for i in range(1, N):
        if arrA == arrB:
           return 1
        
        loc = i - 1
        tmp = arrA[i]
    
        while 0 <= loc and tmp < arrA[loc]:
            arrA[loc+1] = arrA[loc]
            if arrA == arrB:
                return 1
            loc -= 1
            
        if loc + 1 != i:
            arrA[loc + 1] = tmp
            
    return 0

print(solution(N, arrA, arrB))

