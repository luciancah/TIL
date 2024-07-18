n = int(input())

s = set()
for i in range(n):
    opr, num = map(str, input().split())
    num = int(num)

    if opr == "find":
        if num in s:
            print('true')
        else:
            print('false')
    elif opr == "add":
        s.add(num)
    elif opr == "remove":
        s.remove(num)