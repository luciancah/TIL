import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n = 6
expression = input()
num = [0 for _ in range(n)]
ans = INT_MIN


def conv(idx):
    return num[ord(expression[idx]) - ord('a')]


def calc():
    length = len(expression)
    value = conv(0)
    for i in range(2, length, 2):
        if expression[i - 1] == '+':
            value += conv(i)
        elif expression[i - 1] == '-':
            value -= conv(i)
        else:
            value *= conv(i)
    return value


# 'a'부터 'f'까지 순서대로
# 0부터 5번째 index까지의 값을 
# 1~4 중에 하나로 채웁니다.
def find_max(cnt):
    global ans
    
    if cnt == n:
        ans = max(ans, calc())
        return
    
    for i in range(1, 5):
        num[cnt] = i
        find_max(cnt + 1)

find_max(0)
print(ans)