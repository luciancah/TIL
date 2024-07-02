// n = int(input())
// arr =[[0,0]] +  [list(map(int, input().split())) for _ in range(n*2)]

// # dp[i][j] = 빨간색 i번까지 봤을 때 빨간색 j개 뽑았을때 최대의 합, 답: dp[2n][n]

// dp = [[-1] * (2*n+1) for _ in range(2*n+1)]
// dp[0][0] = 0

// # for i in range(1, 2*n+1):
// #     dp[i][0] = dp[i-1][0] + arr[i][0]
// #     dp[0][i] = dp[0][i-1] + arr[i][1]

// for i in range(1, 2*n+1):
//     for j in range(i+1):
//         # # i번 빨간색 뽑고 j 안뽑는 경우
//         if j > 0:
//             dp[i][j] = max(dp[i-1][j-1] + arr[i][0], dp[i][j])
//         if i -j > 0:
//             dp[i][j] = max(dp[i-1][j] + arr[i][1], dp[i][j])


// print(dp[2*n][n])

const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split("\n")
const int_min = Number.MIN_SAFE_INTEGER

const n = Number(input[0])
const cards = new Array(2*n+1).fill([0, 0])

for (let i = 1; i <= 2 * n; i++) {
    const [r, b] = input[i].split(' ').map(Number)
    cards[i] = [r, b]
}

const dp = Array.from(Array(2*n+1), () => new Array(2*n+1).fill(0))

for (let i = 0; i < 2*n+1; i++) {
    for (let j =0; j < 2*n+1; j++) {
        dp[i][j] = int_min
    }
}

dp[0][0] = 0

for (let i = 1; i < 2*n+1; i++) {
    for (let j = 0; j < 2*n+1; j++) {
        if (j > 0) {
            dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1] + cards[i][0])
        }

        if (i - j > 0) {
            dp[i][j] = Math.max(dp[i][j], dp[i-1][j] + cards[i][1])
        }
    }
}

console.log(dp[2*n][n])