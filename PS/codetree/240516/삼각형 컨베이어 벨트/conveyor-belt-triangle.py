n, t = list(map(int, input().split()))
arr = []
for i in range(3):
    arr += list(map(int,input().split()))

for i in range(t):
    last = arr.pop()
    arr.insert(0, last)

print(*arr[:len(arr)//3])
print(*arr[len(arr)//3:(len(arr)//3)*2])
print(*arr[(len(arr)//3)*2:])