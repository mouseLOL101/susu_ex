
def YAH(a, l):
    return max(sum(a)-2*sum(a[w:z])+z-w for w in range(l) for z in range(w+1,l+1))

#  основная программа
l = int(input())
a = list(map(int,input().split()))
if set(a) == 0 or set(a) == 1:
    print(l)
else:
    print(YAH(a, l))


