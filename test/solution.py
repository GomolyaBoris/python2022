from collections import OrderedDict

with open('input.txt') as f:  # открытие файла
    N, M = map(int, f.readline().split(' '))
    grid = []
    ships = [('!', '!')]
    remove = []
    a = []
    for i in range(N):  # cоздание сетки
        b = f.readline()
        grid.append([b[d:d + 1] for d in range(0, len(b) - 1)])
    for j in range(N):  # Поиск горизонтальных тонких кораблей
        for i in range(M - 1):
            if grid[j][i] == '1' and grid[j][i + 1] == '1':
                ships.append([(i, j), (i + 1, j)])
                if ships[-2][-1] == ships[-1][0]:
                    ships[-2].append(ships[-1][1])
                    ships.pop(-1)
                for p in range(len(ships)):
                    for h in range(1, len(ships)):
                        if ships[p][0][0] == ships[h][0][0] and ((
                                int(ships[p][0][1]) - int(ships[h][0][1]) >= 1 and abs(
                            int(ships[h][0][1]) - int(ships[p][0][1])) < 2)):
                            remove.append(ships[p][0])
                            remove.append(ships[p][1])
                            remove.append(ships[h][0])
                            remove.append(ships[h][1])
                            remove = list(OrderedDict.fromkeys(remove))

    for j in range(N - 1):
        for i in range(M - 1):
            if grid[j][i] == '1' and grid[j + 1][i] == '1' and grid[j + 1][i + 1] == '0' and grid[j - 1][i - 1] == '0':
                ships.append([(i, j), (i, j + 1)])
                if ships[-2][-1] == ships[-1][0]:
                    ships[-2].append(ships[-1][1])
                    ships.pop(-1)
    flag = True
    for g in range(len(ships)):  # удаление лишних элементов
        flag = True
        for k in range(len(remove)):
            for q in range(len(ships[g])):
                if ships[g][q] == remove[k]:
                    flag = False

        if flag:
            a.append(ships[g])
    ships = a
    for j in range(N - 1):  # поиск широких кораблей
        for i in range(M - 1):
            if grid[j][i] == '1' and grid[j][i + 1] == '1' and grid[j + 1][i] == '1' and grid[j + 1][i + 1] == '1':
                ships.append([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
                if ships[-2][-1] == ships[-1][1]:
                    ships[-2].append(ships[-1][2])
                    ships[-2].append(ships[-1][3])
                    ships.pop(-1)
    for j in range(1, N - 1):  # Поиск одинночные корабли в сетке не включая контур
        for i in range(1, M - 1):
            if (j != 0 and i != 0) or (j != N and i != 0) or (j != 0 and i != M) or (j != N and i != M):
                if grid[j][i] == '1' and grid[j][i + 1] == '0' and grid[j + 1][i] == '0' and grid[j][i - 1] == '0' and \
                        grid[j - 1][i] == '0':
                    ships.append([(i, j)])
    for j in range(N):  # Поиск одинночные корабли на контуре сетки
        for i in range(M):
            if j == 0 and i != M - 1 and i != 0:
                if grid[j][i] == '1' and grid[j + 1][i] == '0' and grid[j][i + 1] == '0' and grid[j][i - 1] == '0':
                    ships.append([(i, j)])
            elif j == N - 1 and i != M - 1 and i != 0:
                if grid[j][i] == '1' and grid[j - 1][i] == '0' and grid[j][i + 1] == '0' and grid[j][i - 1] == '0':
                    ships.append([(i, j)])
            elif i == 0 and j != N - 1 and j != 0:
                if grid[j][i] == '1' and grid[j][i + 1] == 0 and grid[j + 1][i] == '0' and grid[j - 1][i] == '0':
                    ships.append([(i, j)])
            elif i == M - 1 and j != N - 1 and j != 0:
                if grid[j][i] == '1' and grid[j][i - 1] == 0 and grid[j + 1][i] == '0' and grid[j - 1][i] == '0':
                    ships.append([(i, j)])
            elif j == 0 and i == 0:
                if grid[j][i] == '1' and grid[j + 1][i] == '0' and grid[j][i + 1] == '0':
                    ships.append([(i, j)])
            elif j == 0 and i == M - 1:
                if grid[j][i] == '1' and grid[j + 1][i] == '0' and grid[j][i - 1] == '0':
                    ships.append([(i, j)])
            elif j == N - 1 and i == 0:
                if grid[j][i] == '1' and grid[j - 1][i] == '0' and grid[j][i + 1] == '0':
                    ships.append([(i, j)])
            elif j == N - 1 and i == M - 1:
                if grid[j][i] == '1' and grid[j - 1][i] == '0' and grid[j][i - 1] == '0':
                    ships.append([(i, j)])

d = []
a.pop(0)
for i in range(len(a)):  # Высчитываем размер
    if len(a[i]) > 1:
        d.append([int(a[i][-1][0]) - int(a[i][0][0]) + 1, int(a[i][-1][1]) - int(a[i][0][1]) + 1])
    else:
        d.append([1, 1])
s = []
q = []
for i in range(len(d)):  # Счёт кораблей с одиннаковым размером
    c = 1
    for j in range(len(d)):
        if i != j and ((d[i][0] == d[j][1] and d[i][1] == d[j][0]) or (d[i][0] == d[j][0] and d[i][1] == d[j][1])):
            if d[i][0] == d[j][1] and d[i][1] == d[j][0]:
                d[j][1] = d[i][1]
                d[j][0] = d[i][0]

            c += 1
    if d[i][1] > d[i][0]:
        d[i][1], d[i][0] = d[i][0], d[i][1]
    if not d[i] in s:  # Не включаем элементы, который повторяются
        s.append(d[i])
        q.append([c, d[i]])

for i in range(len(q)): # сортируем по второму столбцу
    for j in range(i, len(q)):
        if q[i][1][0] > q[j][1][0]:
            q[i], q[j] = q[j], q[i]
        if q[i][1][0] == q[j][1][0] and q[i][1][1] > q[j][1][1]:
            q[i], q[j] = q[j], q[i]
with open('output.txt', 'w') as f:
    for i in range(len(q)):
        f.write(f'{q[i][1][0]} {q[i][1][1]} {q[i][0]}\n')
