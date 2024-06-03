n = int(input())
ans1 = []
ans2 = []

def recur1(n):
    if n == 0:
        return
    ans1.append(n)
    recur1(n-1)
    ans1.append(n)

recur1(n)

print(*ans1)