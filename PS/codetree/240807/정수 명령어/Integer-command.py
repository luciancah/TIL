from sortedcontainers import SortedSet

t = int(input())

for _ in range(t):
    s = SortedSet()
    k = int(input())

    for _ in range(k):
        opr = list(map(str, input().split()))
        
        if opr[0] == "I":
            s.add(int(opr[1]))
        elif opr == ["D", "1"]:
            if s:
                s.remove(s[-1])
        elif opr == ["D", "-1"]:
            if s:
                s.remove(s[0])
        
    if s:
        print(s[-1], s[0])
    else:
        print('EMPTY')