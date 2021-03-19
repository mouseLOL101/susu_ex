def Lev(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    f = [[max(i, j) if min(i,j) == 0 else 0 for i in range(len(b) + 1)]
         for j in range(len(a)+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i-1][j-1]

            else:
                f[i][j] = 1 + min(
                    f[i][j - 1],
                    f[i - 1][j],
                    f[i - 1][j - 1]
                )

    return f[-1][-1]


# основная программа

ans =[]
with open('error.txt') as err:
    for j in range(4):
        s_err = err.readline()
        temp = 10000000
        with open('address.txt') as add:
            for i in range(80):
                s_add = add.readline()
                d = Lev(s_add, s_err)
                #d = distance(s_add, s_err)
                if d < temp:
                    temp = d
                    mb_ans = s_add

        ans.append([int(i) for i in mb_ans.split() if i.isdigit()])

for i in ans:
    print(*i, end = '')





