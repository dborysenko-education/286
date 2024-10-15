height = float(input("Введіть ваш зріст, м: "))
weight = float(input("Введіть вашу вагу, кг: "))

imt = weight / (height * height)

print(f"Ваш індекси маси тіла = {imt}%", end="")

if imt < 18.5: 
    verdict = "Недостатня маса"
elif imt >= 18.5 and imt < 24.9: 
    verdict = "Норма"
elif imt >= 25 and imt < 29.9: 
    verdict = "Передожиріння (гладкість)"
elif imt >= 30 and imt < 34.9: 
    verdict = "Ожиріння I ступеня"
elif imt >= 35 and imt < 39.9: 
    verdict = "Ожиріння II ступеня"
elif imt >= 40 and imt < 44.9: 
    verdict = "Ожиріння III ступеня"
else: 
    verdict = "Смерть"
print(f", {verdict}")

