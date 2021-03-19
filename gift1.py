"""
ID: sinelni1
LANG: PYTHON3
TASK: gift1
"""

def D(name, n):
    for i in range(n):
        temp_n = f.readline()
        n1, n2 = f.readline().split()
        n1 = int(n1); n2 = int(n2)
        if n2 != 0:
            div_sum = n1 // n2
            rem = n1 - n1 % n2
            name[temp_n.replace('\n', '')] -= rem
        for i in range(n2):
            temp_n = f.readline()
            name[temp_n.replace('\n', '')] += div_sum
    return name


def Enum(n):
    name = {}
    for i in range(n):
        temp_n = f.readline()
        name[temp_n[:-1]] = 0
    name = D(name, n)
    return name


# основная программа
with open('gift1.in') as f:
    n = int(f.readline())
    name = Enum(n)

with open('gift1.out', 'w') as f:
    for key, value in name.items():
        f.write("{0} {1}".format(key, value) + '\n')

