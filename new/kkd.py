parameter_names = ["Довжина похилої площини", "Маса", "Висота", "Сила"]
print("Введіть параметри для розрахунку ККД похилої площини: ")

parameter_values = []
for parameter in parameter_names: 
    parameter_values.append(int(input(f"{parameter}: ")))
g = 9.8
kkd = (parameter_values[1] * g * parameter_values[2]) / (parameter_values[0] * parameter_values[3]) 

print(f"ККД Похилої площини з введеними параметраи = {kkd}%")
