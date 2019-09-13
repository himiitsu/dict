import random
import sys

#Выбираем случайный индекс за исключением индекса n
def excludingRandom(out, n):
    length = len(out)
    res = list(range(0, n)) + list(range(n + 1, length))
    return random.choice(res)

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
        result[j].append("A")
        i = i + 1
    j = j + 1
    i = 0



result[0][0] = states[2]
i = 0
j = 0
while j <= length:
    if result[0][0] == 'S':
        result[j][i+1] = states[excludingRandom(states, 0)]
        j = j + 1
        continue
    result[j].append(random.choice(states))
    j = j + 1


i = 0
while i < len(result):
    print(result[i])
    i = i + 1

print(result[0][1])