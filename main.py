import random
import sys

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

while j <= length:
    result[j].append(random.choice(states))
    result[j].append(random.choice(states))
    j = j + 1

i = 0
while i < len(result):
    print(result[i])
    i = i + 1

print(result[0][1])