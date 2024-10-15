import random 
guess_from = 300
guess_to = 600
secret = random.randint(guess_from,guess_to)
attempts = 0
while True: 
    guess = int(input(f"Вгадайте число від {guess_from} до {guess_to}: "))
    attempts += 1
    if guess == secret: 
        print(f"Ура! Ви виграли! Вам знадобилось стільки спроб: {attempts}")
        break
    elif guess > secret: 
        print(f"Загадане число МЕНШЕ від {guess}")
    else: 
        print(f"Загадане число БІЛЬШЕ від {guess}")