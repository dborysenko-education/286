import random
secret = random.randint(1, 100)
attempts = 0
while True: 
    guess = int(input("Введіть число від 1 до 100: "))
    attempts += 1
    if guess == secret: 
        print(f"Ура! Ви вгадали! Загадане число -- {secret}. Ви вгадали з такої спроби: {attempts}")
        break
    elif guess > secret: 
        print(f"Загадане число МЕНШЕ ніж {guess}!")
    else: 
        print(f"Загадане число БІЛЬШЕ ніж {guess}!")