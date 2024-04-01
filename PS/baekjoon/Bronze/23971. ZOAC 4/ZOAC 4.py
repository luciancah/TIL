h, w, n, m = list(map(int, input().split()))
# 5 4 1 1
# x -> 5 // 2

x = (h + n) // (n + 1)
y = (w + m) // (m + 1)

print(x * y)