// # 가능한 가짓수 구하는 문제 -> 2차원으로 해야댐
// # dp[i][j] -> i번 숫자까지 고려했을 때 j가 나오는 서로 다른 가짓수
// # 가짓수 : i번 숫자 뺀경우 / 더한경우

// n, m = map(int, input().split())
// arr = [0] + list(map(int, input().split()))


// dp = [[0 for _ in range(41)] for _ in range(n+1)]

// dp[0][20] = 1
// m += 20

// for i in range(1, n+1):
//     for j in range(0, 41):
//         if j + arr[i] <= 40:
//             dp[i][j] += dp[i-1][j + arr[i]]
        
//         if j - arr[i] >= 0:
//             dp[i][j] += dp[i-1][j - arr[i]]

// print(dp[n][m])

const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split('\n')

let [n, m] = input[0].split(' ').map(Number)
let arr = [0]
arr.push(...input[1].split(' ').map(Number))

const offset = 20
const dp = Array.from(Array(n+1), () => Array(41).fill(0n))

dp[0][offset] = 1n
m += 20

for (let i = 1; i < n+1; i++) {
    for (let j = 0; j < 41; j++) {
        if (j + arr[i] <= 40) {
            dp[i][j] = dp[i][j] + dp[i-1][j+arr[i]]
        }

        if (j - arr[i] >= 0) {
            dp[i][j] = dp[i][j] + dp[i-1][j-arr[i]]
        }
    }
}

console.log(dp[n][m].toString())