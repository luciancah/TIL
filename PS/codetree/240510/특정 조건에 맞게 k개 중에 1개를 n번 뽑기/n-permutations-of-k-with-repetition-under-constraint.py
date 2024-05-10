K, N = map(int, input().split())

res = []
def print_res():
    for elem in res:
        print(elem, end=" ")
    print()

def C(n):
    if n == N + 1:
        print_res()
        return
    for i in range(1, K + 1):
        if n >= 3 and i == res[-1] == res[-2]:
            continue
        res.append(i)
        C(n + 1)
        res.pop()

C(1)