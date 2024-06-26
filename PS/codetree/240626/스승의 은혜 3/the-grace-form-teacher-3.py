n, m = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(n)]
gifts2 = gifts[:]
gifts.sort(key=lambda x: (x[0]+x[1]))
gifts2.sort(key=lambda x: (x[0] // 2 + x[1]))

max_ans = 0
for i in range(n):
    price = 0
    ans = n
    for j in range(n):
        if i == j:
            price += gifts[j][0] // 2 + gifts[j][1]
        else:
            price += gifts[j][0] + gifts[j][1]
        if price > m:
            ans = j
            # print(i, j, price, m, ans, max_ans)
            break
    max_ans = max(ans, max_ans)

max_ans2 = 0
for i in range(n):
    price = 0
    ans = n
    for j in range(n):
        if i == j:
            price += gifts2[j][0] // 2 + gifts2[j][1]
        else:
            price += gifts2[j][0] + gifts2[j][1]
        if price > m:
            ans = j
            # print(i, j, price, m, ans, max_ans)
            break
    max_ans2 = max(ans, max_ans2)


print(max(max_ans, max_ans2))