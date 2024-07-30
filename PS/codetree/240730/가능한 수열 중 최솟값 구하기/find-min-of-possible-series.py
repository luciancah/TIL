n = int(input())
seq = []
nums = [4, 5, 6]
candidates = []

def is_possibe(idx, r):
    global seq
    if idx + 2 * r > len(seq):
        return True
    start_1 = idx
    start_2 = idx + r
    for i in range(r):
        if seq[start_1 + i] != seq[start_2 + i]:
            return is_possibe(idx, r + 1)
    return False

def append_num():
    global seq, candidates
    seq_len = len(seq)
    if seq_len > n: return
    for i in range(seq_len):
        if is_possibe(i, 1) == False:
            return
    if seq_len == n:
        for i in range(len(seq)):
            print(seq[i], end='')
        exit()
    for i in range(3):
        seq.append(nums[i])
        append_num()
        seq.pop()
    
append_num()
candidates.sort()
for i in range(len(candidates[0])):
    print(candidates[0][i], end='')