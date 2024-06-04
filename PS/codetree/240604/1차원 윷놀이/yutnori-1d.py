n, m, k = list(map(int, input().split()))
moves = list(map(int, input().split()))

# moves를 n개의 말에 배분하는 조합

answers = [1 for _ in range(k)]

def calc(answers):
    return len([x for x in answers if x >= m])

max_ans = 0
def choose(count):
    global max_ans
    if count == n:
        max_ans = max(max_ans, calc(answers))
        return

    for i in range(len(answers)):
        answers[i] += moves[count]
        choose(count + 1)
        answers[i] -= moves[count]

    return

choose(0)

print(max_ans)