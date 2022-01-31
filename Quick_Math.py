import time
import random

met = ['+', '-', '*', '/']

try:
    tim = int(input('Number of seconds: '))
except ValueError:
    print('Error, please write number of seconds again')
    tim = int(input('Number of seconds: '))

method = str(input('+, -, *, / : '))
if method not in met:
    print('Error, enter method correctly')
    method = str(input('+, -, *, / : '))
else:
    method = method
    
# entering value of numbers in further example: 1 20 
min, max = input('Enter min/max value of numbers: ').split()
min = int(min)
max = int(max)

score = 0

# Addition test
if method == '+':
    while True:
        a = random.randint(min, max)
        b = random.randint(min, max)

        start = time.time()
        print(f'{a} + {b}')
        res = a + b
        respond = int(input())

        end = time.time()

        total = end - start
        if total > tim:
            print('Time is over')
            print('Score: ', score)
            break
        if respond == res and total <= tim:
            print("Correct\n")
            score += 1
            continue
        else:
            print('Uncorrect\n')
            print(f'Correct answer: {a} + {b} = {res}')
            print('Your score: ', score)
            break

# Subtraction test
if method == '-':
    while True:
        a = random.randint(min, max)
        b = random.randint(min, max)

        start = time.time()
        res = a - b
        if a < b:
            print(f'{b} - {a}')
            res = b - a
        if a > b:
            print(f'{a} - {b}')
            res = a - b
        if a == b:
            continue

        respond = int(input())

        end = time.time()

        total = end - start

        if total > tim:
            print('Time is over')
            print('Your score: ', score)
        if respond == res and total <= tim:
            print("Correct\n")
            score += 1
            continue

        else:
            if a < b:
                print('Uncorrect\n')
                print(f'Correct answer: {b} - {a} = {res}')
                print('Your score: ', score)
            if a > b:
                print('Uncorrect\n')
                print(f'Correct answer: {a} - {b} = {res}')
                print('Your score: ', score)
            break

# Multiplication test
if method == '*':
    while True:
        a = random.randint(min, max)
        b = random.randint(min, max)

        start = time.time()
        print(f'{a} * {b}')
        res = a * b
        respond = int(input())

        end = time.time()

        total = end - start
        if total > tim:
            print('Time is over\n')
            print('Your score: ', score)
            break
        if respond == res and total <= tim:
            print("Correct\n")
            score += 1
            continue
        else:
            print('Uncorrect\n')
            print(f'Correct answer: {a} * {b} = {res}')
            print('Your score: ', score)
            break

# Division test
if method == '/':
    while True:
        a = random.randint(min, max)
        b = random.randint(min, max)

        start = time.time()

        res = a / b
        if a % b == 0:
            print(f'{a} / {b}')
            res = a / b
        else:
            continue

        respond = int(input())

        end = time.time()

        total = end - start
        if total > tim:
            print('Time is over\n')
            print('Your score: ', score)
            break
        if respond == res and total <= tim:
            print("Correct\n")
            score += 1
            continue
        else:
            print('Uncorrect\n')
            print(f'Correct answer: {a} / {b} = {res}')
            print('Your score: ', score)
            break
tryagain = input("Game over!")


