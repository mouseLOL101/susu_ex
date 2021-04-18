
n = int(input())

arr = [int(i) for i in input().split()]
maxim = max(arr)
ans = 0
for i in range(n):
    ans += maxim - arr[i]

print(ans)