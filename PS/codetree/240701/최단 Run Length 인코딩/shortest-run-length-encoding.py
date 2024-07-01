A = input()
# If life gives you lemon...
def get_run_length(buf):
    res = ''
    i = 0
    while i < len(buf):
        c = buf[i]
        k = i
        while i < len(buf) - 1 and buf[i] == buf[i + 1]:
            i += 1
        res += c + str(i-k+1)
        i += 1
    # print(res)
    return res

def shift(buf):
    res = buf[0:-1]
    res = buf[-1] + res
    return res

min_len = len(get_run_length(A))

for _ in range(len(A) + 1):
    curr = get_run_length(A)
    if len(curr) < min_len:
        min_len = len(curr)
    A = shift(A)

print(min_len)