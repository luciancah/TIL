a, b, c, d = list(map(int, input().split()))

if ((b < c and a < d) or (d < a and c < b)):
    print('nonintersecting')
else:
    print('intersecting')