import sys

n = int(input())
nums = list(map(int, input().split()))

# nums 순회하면서 고를까 말까로 조합 만들기

group1 = []
group2 = []

min_diff = sys.maxsize

def recur(group1, group2, curr_idx):
    global min_diff
    if curr_idx == 2 * n:
        if len(group1) == n:
            # print(group1, group2)
            diff = abs(sum(group1) - sum(group2))
            min_diff = min(min_diff, diff)
        return

    group1.append(nums[curr_idx])
    recur(group1, group2, curr_idx+1)
    group1.pop()
    group2.append(nums[curr_idx])
    recur(group1, group2, curr_idx+1)
    group2.pop()

recur(group1, group2, 0)

print(min_diff)