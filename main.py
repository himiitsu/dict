import random
import sys
import colorama
from colorama import Fore, Back, Style

#вавыав

def excludingRandom(out, n):
    length = len(out)
    res = list(range(0, n)) + list(range(n + 1, length))
    return random.choice(res)

def litChoose(input, states, i, j):
    if result[i][j] == 'S' and result[i - 1][j + 1] == 'S':
        result[i][j + 1] = states[2]
        j += 1
    elif result[i][j] == 'S' and result[i - 1][j + 1] == 'C':
        result[i][j + 1] = 'S'
        j += 1
    elif result[i][j] == 'S' and result[i - 1][j + 1] == 'L':
        result[i][j + 1] = 'C'
        j += 1
    elif result[i][j] == 'C' and result[i - 1][j + 1] == 'L':
        result[i][j + 1] = states[excludingRandom(states, 2)]
        j += 1
    elif result[i][j] == 'C' and result[i - 1][j + 1] == 'S':
        result[i][j + 1] = 'S'
        j += 1
    elif result[i][j] == 'C' and result[i - 1][j + 1] == 'C':
        result[i][j + 1] = states[excludingRandom(states, 1)]
        j += 1
    elif result[i][j] == 'L' and result[i - 1][j + 1] == 'S':
        result[i][j + 1] = 'C'
        j += 1
    elif result[i][j] == 'L' and result[i - 1][j + 1] == 'L':
        result[i][j + 1] = 'L'
        j += 1
    elif result[i][j] == 'L' and result[i - 1][j + 1] == 'C':
        result[i][j + 1] = 'C'
        j += 1
    return i, j


length, width = 10, 10

states = ["L", "C", "S"]

result = []
result.append([])

i, j = 0, 0

while i < width:
    result.append([])
    i = i + 1

i = 0


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
j = 0
while j < len(result):
    if j == length:
        j = 0
        i += 1
        print()
    if result[i][j] == 'S':
        sys.stdout.write(Fore.BLUE + "S" + Style.RESET_ALL + ' ')
        j += 1
    elif result[i][j] == 'L':
        sys.stdout.write(Fore.GREEN + "L" + Style.RESET_ALL + ' ')
        j += 1
    elif result[i][j] == 'C':
        sys.stdout.write(Fore.YELLOW + "S" + Style.RESET_ALL + ' ')
        j += 1
    if i == length and j == length:
        break