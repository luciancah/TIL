import sys

n = int(input())
ans = []

def is_possible(ans):
    n = len(ans)
    
    for length in range(1, n//2 + 1):
        for i in range(n - 2*length + 1):
            if ans[i:i+length] == ans[i+length:i+2*length]:
                return False
    return True

def recur(ans, count):
    if count == n:
        print(''.join(ans))
        sys.exit()
        return

    for i in range(4, 7):
        temp_ans = ans[:]
        temp_ans.append(str(i))
        if is_possible(temp_ans):
            ans.append(str(i))
            recur(ans, count + 1)
            ans.pop()

recur(ans, 0)