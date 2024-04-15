arr = input()
count = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] == '(' and arr[j] == ')':
            count += 1

print(count)