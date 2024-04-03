y, m, d = list(map(int, input().split()))

def febCheck(y, m, d):
    res = True
    if y % 4 != 0:
        res = False
    if y % 4 == 0 and y % 100 == 0 and y % 400 != 0:
        res = False
    
    if d < 1 or d > 29:
        res = False

    return res

def validCheck(y, m, d):
    days31 = [1, 3, 5, 7, 8, 10, 12]
    if d == 31 and m not in days31:
        return False
    return True


def solution(y, m, d):
    if m == 2:
        if not febCheck(y, m, d):
            print(-1)
            return
    
    if not validCheck(y, m, d):
        print(-1)
        return

    if 3 <= m <= 5:
        print('Spring')
        return

    if 6 <= m <= 8:
        print('Summer')
        return

    if 9 <= m <= 11:
        print('Fall')
        return

    if 1 <= m <= 2 or m == 12:
        print('Winter')
        return


solution(y,m,d)