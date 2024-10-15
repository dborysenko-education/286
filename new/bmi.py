height = float(input("Введіть свій зріст, м: ")) 
mass = int(input("Введіть масу свого тіла, кг: "))

bmi = mass / (height * height)
print(f"Ваш ІМТ = {bmi}", end="")

if bmi < 18.5: 
    res = "Недостатня вага"
elif bmi >= 18.8 and bmi < 24.9: 
    res = "Норма"
elif bmi >= 18.8 and bmi < 24.9: 
    res = "Норма"
elif bmi >= 25 and bmi < 29.9: 
    res = "Передожиріння (гладкість)"
elif bmi >= 30 and bmi < 34.9: 
    res = "Ожиріння I ступеня"
elif bmi >= 35 and bmi < 39.9: 
    res = "Ожиріння II ступеня"
elif bmi >= 40 and bmi < 44.9: 
    res = "Ожиріння III ступеня"
else: 
    res = "Смерть"
print(f", вердикт = {res}")