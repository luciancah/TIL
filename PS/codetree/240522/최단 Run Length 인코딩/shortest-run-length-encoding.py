'''
길이 n인 문자열 a

- rle 하는 함수 만들기
- shift 하는 함수 만들기
- 완탐 돌려서 길이 미니멈 만들기
'''

s = input()

def shift(s):
    last = s[-1]
    new = last + s[:-1]

    return new

def rle(s):
    s = s + '0'
    count = 1
    char = '_'
    ans = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            char = s[i]
            count += 1
        else:
            ans += char
            ans += str(count)
            count = 1
            char = s[i]
    return len(ans)


min_rle_len = 99999
for i in range(len(s)):
    s = shift(s)
    rle_len = rle(s)
    min_rle_len = min(min_rle_len, rle_len)

print(min_rle_len)