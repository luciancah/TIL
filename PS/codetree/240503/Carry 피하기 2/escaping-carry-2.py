n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

ans = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            carry = False

            if nums[i] % 10 + nums[j] % 10 + nums[k] % 10 >= 10:
                carry = True

            if nums[i] % 100 // 10 + nums[j] % 100 // 10 + nums[k] % 100 // 10 >= 10:
                carry = True

            if nums[i] % 1000 // 100 + nums[j] % 1000 // 100 + nums[k] % 1000 // 100 >= 10:
                carry = True

            if nums[i] % 10000 // 1000 + nums[j] % 10000 // 1000 + nums[k] % 10000 // 1000 >= 10:
                carry = True

            if carry == False:
                ans = max(ans, nums[i] + nums[j] + nums[k])


print(ans)