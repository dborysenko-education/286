import random 
from_int = 1
to_int = 1000
secret = random.randint(from_int, to_int)
attempts = 0
while True: 
    guess = int(input(f"Вгадайте число від {from_int} до {to_int}: "))
    attempts += 1
    if guess == secret: 
        print("Перемога буде!")
        break
    elif guess > secret: 
        print(f"Загадане число МЕНШЕ за {guess}!")
    else: 
        print(f"Загадане число БІЛЬШЕ за {guess}!")
print(f"Вам знадобилось стільки спроб: {attempts}")