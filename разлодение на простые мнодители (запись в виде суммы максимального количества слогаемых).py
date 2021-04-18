
def QQ(n):
    a = []
    for i in range(2, n):
        while i <= n**0.5 and n % i == 0:
            a.append(i)
            n //= i
    if n > 1:
        a.append(n)
    if len(a) == 1 and a[0] != 3:
        a = [2]*(n//2-1)   # любое простое можно разлодить на сумму двоек(самых маленьких чисел из простых),
        a.append(3)                                    # но, тк число простое, то и нечётное, вычтем одну и прибавим тройку
    else:
        mp = 1
        for i in a:
            mp *= i
        mp //= min(a)
        a = [min(a)] * mp
    return a, len(a)

#  основная программа
num = int(input())
if num > 1:
    ans, l = QQ(num)

    print(l)
    print(*ans)
