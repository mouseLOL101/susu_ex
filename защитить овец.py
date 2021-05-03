def check(i, j):
    global l, b, arr
    if i == -1 or j == -1 or i == l or j == b:
        return 0
    if arr[i][j] == 'S':
        return 1
    return 0

l, b = map(int, input().split())
arr = []
for i in range(l):
    arr.append(list(input()))

ans = 'Yes'
for i in range(l):
    for j in range(b):
        if arr[i][j] == '.':
                arr[i][j] = 'D'
        elif arr[i][j] == 'W':
            if check(i + 1, j) or check(i - 1, j) or check(i, j + 1) or check(i, j - 1):
                ans = 'No'
print(ans)

if ans == 'Yes':
    for i in range(l):
        print(''.join(arr[i]))
