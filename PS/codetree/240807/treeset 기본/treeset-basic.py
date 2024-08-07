from sortedcontainers import SortedSet

# 변수 선언 및 입력:
n = int(input())
s = SortedSet()

for _ in range(n):
    command = input()

    if command.startswith("add"):
        x = int(command.split()[1])
        s.add(x)

    elif command.startswith("remove"):
        x = int(command.split()[1])
        s.remove(x)
    
    elif command.startswith("find"):
        x = int(command.split()[1])
        print("true" if x in s else "false")

    elif command.startswith("lower_bound"):
        x = int(command.split()[1])
        idx = s.bisect_left(x)
        
        # 존재하는 경우에는 해당 값을 출력합니다.
        if idx < len(s):
            print(s[idx])
        else:
            print("None")

    elif command.startswith("upper_bound"):
        x = int(command.split()[1])
        idx = s.bisect_right(x)

        # 존재하는 경우에는 해당 값을 출력합니다.
        if idx < len(s):
            print(s[idx])
        else:
            print("None")
            
    elif command == "largest":
        # 존재하는 경우에는 해당 값을 출력합니다.
        if s:
            print(s[-1])
        else:
            print("None")
            
    else:
        # 존재하는 경우에는 해당 값을 출력합니다.
        if s:
            print(s[0])
        else:
            print("None")