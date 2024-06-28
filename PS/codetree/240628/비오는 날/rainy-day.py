n = int(input())
arr = [list(map(str,input().split())) for _ in range(n)]

# def convert_day(date):
#     year,month,day = date.split()

arr.sort(key=lambda x:x[0])
for a,b,c in arr:
    if c == 'Rain':
        print(a,b,c)
        break