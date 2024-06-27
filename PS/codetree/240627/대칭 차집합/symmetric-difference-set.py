n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)

c1 = a - b
c2 = b - a

print(len(c1.union(c2)))