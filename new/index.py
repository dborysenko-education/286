height = float(input("Введіть свій зріст у метрах: "))
weight = float(input("Введіть свою вагу в кілограмах: "))

bmi = weight / (height * height)

print(f"ІМТ: {bmi}%, ", end="")

if bmi < 18.5: 
    explanation = "Недостатня маса"
elif bmi >= 18.5 and bmi < 25: 
    explanation = "Норма"
elif bmi >= 25 and bmi < 30: 
    explanation = "Передожиріння (гладкість)"
elif bmi >= 30 and bmi < 35: 
    explanation = "Ожиріння I ступеня"
elif bmi >= 35 and bmi < 40: 
    explanation = "Ожиріння II ступеня"
elif bmi >= 40 and bmi < 45: 
    explanation = "Ожиріння III ступеня"
else: 
    explanation = "СМЕРТЬ"

print(explanation)