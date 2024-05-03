n, t = map(int, input().split())
first_l = [int(x) for x in input().split()]
second_l = [int(x) for x in input().split()]

for _ in range(t):
    temp = first_l[-1]
    for i in range(len(first_l) - 1, 0, -1):
        first_l[i] = first_l[i - 1]
    first_l[0] = second_l[-1]
    for i in range(len(second_l) - 1, 0, -1):
        second_l[i] = second_l[i - 1]
    second_l[0] = temp

print(*first_l)
print(*second_l)