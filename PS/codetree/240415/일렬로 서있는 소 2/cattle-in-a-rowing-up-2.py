n = int(input())
cows = list(map(int, input().split()))
count = 0

for i in range(len(cows)):
    for j in range(i + 1, len(cows)):
        for k in range(j + 1, len(cows)):
            if cows[i] <= cows[j] and cows[j] <= cows[k]:
                count += 1

print(count)