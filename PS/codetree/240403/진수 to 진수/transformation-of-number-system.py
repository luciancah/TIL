a, b = list(map(int, input().split()))
n = int(input())

# a진수 n -> 10진수 m으로 바꾸기
m = int(str(n), a)

def calc(num, base, ans=''):
    if num == 0:
        ans = ans[::-1]
        print(ans)

        return ans
    ans += str(num % base)
    calc(num // base, base, ans)

calc(m, b)