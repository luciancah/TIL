k, n = map(int, input().split())
res = []

def print_res():
    for elem in res:
        print(elem, end=" ")
    print()

#1~k n번 반복
def C(cur_n):
    if cur_n == n + 1:
        print_res()
        return;
    for i in range(1, k + 1):
        res.append(i)
        C(cur_n + 1)
        res.pop()

C(1)