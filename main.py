import random
import sys

#Выбираем случайный индекс за исключением индекса n
def excludingRandom(out, n):
    length = len(out)
    res = list(range(0, n)) + list(range(n + 1, length))
    return random.choice(res)

def litChoose(input, states, i, j):
    if result[i][j] == 'S' and result[i - 1][j + 1] == 'S':
        result[i][j + 1] = states[excludingRandom(states, 0)]
        j += 1
    elif result[i][j] == 'S' and result[i - 1][j + 1] == 'C':
        result[i][j + 1] = states[excludingRandom(states, 0)]
        j += 1
    elif result[i][j] == 'S' and result[i - 1][j + 1] == 'L':
        result[i][j + 1] = 'C'
        j += 1
    elif result[i][j] == 'C' and result[i - 1][j + 1] == 'L':
        result[i][j + 1] = states[excludingRandom(states, 2)]
        j += 1
    elif result[i][j] == 'C' and result[i - 1][j + 1] == 'S':
        result[i][j + 1] = states[excludingRandom(states, 0)]
        j += 1
    elif result[i][j] == 'C' and result[i - 1][j + 1] == 'C':
        result[i][j + 1] = random.choice(states)
        j += 1
    elif result[i][j] == 'L' and result[i - 1][j + 1] == 'S':
        result[i][j + 1] = 'C'
        j += 1
    elif result[i][j] == 'L' and result[i - 1][j + 1] == 'L' or 'C':
        result[i][j + 1] = states[excludingRandom(states, 2)]
        j += 1
    return i, j

UP = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DOWN = (0, -1)

length, width = 10, 10

states = ["L", "C", "S"]

result = []
result.append([])

i, j = 0, 0

while i < width:
    result.append([])
    i = i + 1

i = 0

#заполняем всю матрицу элементом неопределённости "А"
while j <= length:
    while i <= width:
        result[j].append("N")
        i = i + 1
    j = j + 1
    i = 0



i = 0
j = 0

result[i][j] = random.choice(states)

while j <= length:
    if j == length:
        j = 0
        i += 1
        if result[i-1][j] == 'S':
            result[i][j] = states[excludingRandom(states, 0)]
        elif result[i-1][j] == 'C':
            result[i][j] = random.choice(states)
        elif result[i-1][j] == 'L':
            result[i][j] = result[i][j+1] = states[excludingRandom(states, 2)]

    if i == 0:
        if result[i][j] == 'S':
            result[i][j+1] = states[excludingRandom(states, 0)]
            j += 1
        elif result[i][j] == 'C':
            result[i][j + 1] = random.choice(states)
            j += 1
        elif result[i][j] == 'L':
            result[i][j + 1] = states[excludingRandom(states, 2)]
            j += 1

    if i != 0:
        i, j = litChoose(result[i][j], states, i, j)

    if i == length and j == length:
        break



i = 0
while i < len(result):
    print(result[i])
    i = i + 1
