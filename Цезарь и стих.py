
n = 9 ** 3
alf = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
       'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
ALF = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
       'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
ans = []

d = {}
D = {}
for i in range(33):
    d[alf[i]] = alf[(i + n) % 33]
for i in range(33):
    D[ALF[i]] = ALF[(i + n) % 33]


with open('../контесты/file стих') as f:
    for i in range(8):
        temp = ' '
        line = f.readline()

        for j in line:
            if temp == ' ':
                if j in alf:
                    ans.append(d[j])
                elif j in ALF:
                    ans.append(D[j])
            if j in alf:
                j = d[j]
            elif j in ALF:
                j = D[j]

            temp = j

print(*ans, sep = '')





