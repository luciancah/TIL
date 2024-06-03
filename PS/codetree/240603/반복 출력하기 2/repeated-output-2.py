n = int(input())

def recur(n):
    if n == 0:
        return
    print('HelloWorld')
    recur(n-1)

recur(n)