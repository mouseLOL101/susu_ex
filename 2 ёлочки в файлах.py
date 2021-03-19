
dif = []
ind = 0
cnt = 0
with open('file 1.txt') as f1:
    with open('file 2.txt') as f2:

        for c in range(5):
            for i in range(10 + ind):
                lines_1 = f1.readline()
                lines_2 = f2.readline()

                if lines_1 != lines_2:
                    for j in range(len(lines_1)):
                        if lines_1[j] != lines_2[j]:
                            cnt += 1
            dif.append(cnt)
            cnt = 0
            ind += 1

ans = dif[0]**2 + dif[1]**4 * dif[4]**3 + dif[2]**3 * dif[3]**5

print(ans)
print(dif)
