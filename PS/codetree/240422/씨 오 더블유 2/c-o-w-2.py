n = int(input())
input_string = input()
count = 0

for i in range(n):
    if input_string[i] == 'C':
        for j in range(i, n):
            if input_string[j] == 'O':
                for k in range(j, n):
                    if input_string[k] == 'W':
                        count += 1

print(count)