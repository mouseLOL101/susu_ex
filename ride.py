"""
ID: sinelni1
LANG: PYTHON3
TASK: ride
"""

def prod(A):
    k = 1
    for i in A:
        k *= i
    return k

"""def conv(S):
    res = []
    for i in S:
        # res.append(ord(i) - ord('A') + 1)
        res.append(ord(i) - ord('A') + 1)
    return res"""

def conv(S):
    return [ord(i) % 32 for i in S]


def compare(s1, s2):
    return 'GO\n' if int(prod(conv(s1)) % 47) == int(prod(conv(s2)) % 47) else 'STAY\n'


# основная программа
with open('../ride.in') as fi:
    s = fi.read().splitlines()

with open('../ride.out', 'w') as fo:
    fo.write(compare(s[0], s[1]))
