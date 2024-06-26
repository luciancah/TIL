x, y = map(int, input().split())

def is_palindrome(num):
    return list(str(num)) == list(reversed(list(str(num))))

count = 0
for i in range(x, y+1):
    if is_palindrome(i):
        count += 1

print(count)