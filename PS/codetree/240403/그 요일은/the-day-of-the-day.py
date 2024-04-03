m1, d1, m2, d2 = map(int, input().split())
day = input()
daysDiff = 0
dates = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

if m1 < m2:
    # 사이에 온전한 월의 일들 더하기
    if m2 - m1 >= 1:
        for i in range(m1+1, m2):
            daysDiff += dates[i]
            
    # m1월의 d1일부터 말일까지 남은 일 더하기
    daysDiff += (dates[m1] - d1)

    # m2월의 d2일만큼 더하기
    daysDiff += d2

    # A요일 diff만큼 빼기
    daysDiff -= days.index(day)

else:
    daysDiff += (d2 - d1)
    daysDiff -= days.index(day)

print(daysDiff // 7 + 1 if daysDiff >= 0 else 0)