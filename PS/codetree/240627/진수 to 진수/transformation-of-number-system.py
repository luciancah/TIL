a, b = map(int, input().split())
n = input()

num = int(n, a)
ans = []

while num > 0:
    ans.append(str(num % b))
    num = num // b

ans.reverse()

print(''.join(ans))