m1, d1, m2, d2 = map(int, input().split())
day = input()
day_map = {
    'Mon': 0,
    'Tue': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4,
    'Sat': 5,
    'Sun': 6
}
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ans = 0
for i in range(m1, m2+1):
    if m1 == m2:
        ans += d2 - d1
        continue
    elif i == m1:
        ans += months[i] - d1
        continue
    elif i == m2:
        ans += d2
        continue
    ans += months[i]

# print(ans)
ans = ans - day_map[day]
print(ans//7 + 1)