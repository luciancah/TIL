n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

arr2 = [x for x in arr if x[2] == 'Rain']
arr2.sort(key=lambda x : x[0])

print(' '.join(arr2[0]))