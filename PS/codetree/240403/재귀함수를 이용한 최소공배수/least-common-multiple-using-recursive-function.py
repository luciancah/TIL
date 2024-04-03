n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm_of_list(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    else:
        return lcm(arr[index], find_lcm_of_list(arr, index+1))

print(find_lcm_of_list(arr))