n = int(input())
copyn = n

def star(n):
    if n == 0:
        return

    print('* ' * n)
    star(n-1)

def revStar(n):
    if n > copyn:
        return

    print('* ' * n)
    revStar(n+1)

star(n)
revStar(1)