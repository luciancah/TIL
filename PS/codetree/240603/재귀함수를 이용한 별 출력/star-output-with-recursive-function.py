n = int(input())
ans1 = []

def recur1(n):
    if n == 0:
        return
    recur1(n-1)
    print('*'*n)

recur1(n)