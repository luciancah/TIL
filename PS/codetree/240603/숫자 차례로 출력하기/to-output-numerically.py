n = int(input())
ans1 = []
ans2 = []

def recur1(n):
    if n == 0:
        return
    ans1.append(n)
    recur1(n-1)

def recur2(n):
    if n == 0:
        return
    recur2(n-1)
    ans2.append(n)

recur1(n)
recur2(n)

print(*ans2)
print(*ans1)