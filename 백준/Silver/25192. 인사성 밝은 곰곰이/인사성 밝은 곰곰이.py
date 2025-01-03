# from sys.stdin import readline
# import sys.stdin.readline

# n = readline()
n = int(input())

cnt = 0
name_set = set()
for _ in range(n):
    # name = readline().strip()
    name = input()
    if name == "ENTER":
        cnt += len(name_set)
        name_set = set()
        continue
    name_set.add(name)
    
cnt += len(name_set)
print(cnt)
        
    
