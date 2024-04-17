number = list(input())
max_list = []

for i in range(len(number)):
    new_number = number[:]
    if number[i] == '0':
        new_number[i] = '1'
    else:
        new_number[i] = '0'
    max_list.append(int(''.join(new_number), 2))
    

print(max(max_list))