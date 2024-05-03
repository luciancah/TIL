n = int(input())
lst = []
buf = []
for _ in range(n):
    lst.append(int(input()))
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
for i in range(n):
    if i < s1-1 or i > e1-1:
        buf.append(lst[i])
lst = buf
n = len(buf)
buf = []
for i in range(n):
    if i < s2-1 or i > e2-1:
        buf.append(lst[i])
print(len(buf))
for i in range(len(buf)):
    print(buf[i])