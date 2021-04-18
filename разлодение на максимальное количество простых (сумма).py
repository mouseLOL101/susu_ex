def SUM(n):
    if n % 2:
        a = [2] * (n//2-1) + [3]
    else:
        a = [2] * (n//2)
    return a, len(a)

#  основаная программа
num = int(input())
a, l = SUM(num)
print(l)
print(*a)