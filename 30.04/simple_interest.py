deposit = int(input("Введіть сумму, яку кладете на депозит: "))
interest = int(input("Введіть ставку річного проценту, %: "))
years = int(input("На скільки років влкадаєте гроші під простий процент: "))

after_all_year = deposit + years*deposit*interest/100

print(f"Наприкінці терміну сума вашого влкаду з відсотками складатиме: {after_all_year}")