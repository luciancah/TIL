buf = list(input())
# Check what we got for alphabets
alphabets = {}
n = len(buf)
for i in range(len(buf)):
    if i % 2 == 0:
        alphabets[buf[i]] = 1

res = -(2**31)


def compute_and_compare(curr_a):
    global res
    val = curr_a[buf[0]]
    for i in range(1, n, 2):
        if buf[i] == "+":
            val += curr_a[buf[i + 1]]
        if buf[i] == "-":
            val -= curr_a[buf[i + 1]]
        if buf[i] == "*":
            val *= curr_a[buf[i + 1]]
    res = max(res, val)


def check_combs(curr_a):
    compute_and_compare(curr_a)

    for k in curr_a.keys():
        if curr_a[k] >= 4:
            continue
        curr_a[k] += 1
        check_combs(curr_a)
        curr_a[k] -= 1


check_combs(alphabets)
print(res)