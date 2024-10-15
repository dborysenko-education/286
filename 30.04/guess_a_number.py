import random 
secret_number = random.randint(1,100)
attempts = 0
while True: 
    guess = int(input("Guess a number from 1 to 100: "))
    attempts += 1
    if guess == secret_number: 
        print(f"Success! Your attempts: {attempts} ")
        break
    elif guess > secret_number: 
        print(f" Your number is greater than secret number! ")
    else: 
        print(f"Your number is less than secret number! ")