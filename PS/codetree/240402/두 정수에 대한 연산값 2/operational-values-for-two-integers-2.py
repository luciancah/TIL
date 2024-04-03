a, b = list(map(int, input().split()))

def calc(a, b):
    if min(a, b) == a:
        a += 10
        b *= 2
    else:
        a *= 2
        b += 10

    return a, b

a, b = calc(a, b)
print(a, b)