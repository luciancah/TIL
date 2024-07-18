from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for i in range(n):
    operations = list(map(str, input().split()))
    if operations[0] == "add":
        opr = "add"
        key = int(operations[1])
        value = int(operations[2])

        sd[key] = value

    elif operations[0] == "remove":
        opr = "remove"
        key = int(operations[1])

        sd.pop(key)

    elif operations[0] == "find":
        opr = "find"
        key = int(operations[1])

        if key in sd:
            print(sd[key])
        else:
            print("None")

    elif operations[0] == "print_list":
        opr = "find"
        if len(list(sd.items())) == 0:
            print("None")

        print(" ".join(list(map(str, sd.values()))))