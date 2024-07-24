n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a - 1))
lines.sort()
selected_lines = []
ans = m

# 사다리 태움
def run_ladders():
    nums1, nums2 = [i for i in range(n)], [i for i in range(n)]

    for _, idx in lines:
        nums1[idx], nums1[idx + 1] = nums1[idx + 1], nums1[idx]
    for _, idx in selected_lines:
        nums2[idx], nums2[idx + 1] = nums2[idx + 1], nums2[idx]

    for i in range(n):
        if nums1[i] != nums2[i]:
            return False
    return True

# 각 갯수에 대해 가능한 조합을 체크함
def get_min_lines(cnt):
    global ans

    if cnt == m:
        if run_ladders():
            ans = min(ans, len(selected_lines))
        return
    
    selected_lines.append(lines[cnt])
    get_min_lines(cnt + 1)
    selected_lines.pop()
    get_min_lines(cnt + 1)

get_min_lines(0)
print(ans)