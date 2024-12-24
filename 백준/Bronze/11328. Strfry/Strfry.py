import sys

input = sys.stdin.readline
n = int(input().strip())

for _ in range(n):
    s1, s2 = input().strip().split()
    if sorted(list(s1)) == sorted(list(s2)):
        print("Possible")
    else:
        print("Impossible")
    
    