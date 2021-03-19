"""
ID: sinelni1
LANG: PYTHON3
TASK: friday
"""

def Q_DAYS(i, year):
    x = 29 if (i == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)) else 28 \
        if i == 2 else 30 if i in [4, 6, 9, 11] else 31 \
            if i in [1, 3, 5, 7, 8, 10, 12] else "Ошибка! Такого месяца нет."
    return x


# основная программа
with open('friday.in') as f:
    days = [0] * 7; temp = 0
    n = int(f.readline())
    for year in range(1900, 1900 + n):
        for i in range(12):
            days[temp] += 1
            temp = (temp + Q_DAYS(i+1, year) % 7) % 7

with open('friday.out', 'w') as f:
    f.write(' '.join(map(str, days)))
    f.write('\n')



