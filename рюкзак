
# last(r_k, w, s_m)
def Last(a, b, s_m):
    f = [[0 for x in range(b + 1)] for x in range(a + 1)]
    for i in range(1, a + 1):
        for k in range(1, b + 1):    # вес
            if k >= m[i-1]:
                f[i][k] = max(f[i - 1][k - m[i-1]] + v[i-1], f[i - 1][k])
            else:
                f[i][k] = f[i - 1][k]
    k = b
    for i in range(a, 0, -1):
        if f[i][k] != f[i - 1][k]:
            s_m.append(i)
            k -= m[i-1]

    return f[-1][-1], s_m

# 31 наименований подарков, где указаны их вес, значимость и количество
# Ответом будет суммарная значимость всех подарков в мешке и их вес, без пробела
# вес, значимость, количество

n = 31
w = 8000
m = []    # список весов
v = []    # список значимости
r_k = 0

with open('gifts.txt') as f:
    for j in range(n):
        s_f = f.readline()
        l = list(int(i) for i in s_f.split() if i.isdigit())
        r_k += l[2]      # реальное колическтво объектов

        for i in range(l[2]):
            m.append(l[0])
            v.append(l[1])

    s_m = []
    ans2 = 0
    ans1, sum = Last(r_k, w, s_m)
    for j in sum:
        ans2 += m[j-1]
    print(ans1, ans2, sep = ' ')



