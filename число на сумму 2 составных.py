def Test(x):
    i = 2
    while i <= x**0.5:
        if x % i == 0:
            return 1
        else:
            if i == 2: i += 3      # на 3 мы уже проверили
            else: i += 2
    return 0

def Comp(x):
   if x%3 != 0:         # п тесту на простоту Ферма
       if x**(3-1) % 3 != 1:        # если выполняется, то составное, если нет - возможно простое
           print(x**(3-1) % 3)
           return 1
       else:
           return Test(x)
   else: return 1


#  основная программа
num = int(input())
if num >= 12:
    for i in range(4, num - 4 + 1):
        if Comp(i) and Comp(num - i):
            ans1 = i
            ans2 = num - i
            break

    print(i, num - i)
