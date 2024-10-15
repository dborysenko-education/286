deposit = int(input("Введіть сумму, яку кладете на депозит: "))
interest = int(input("Введіть ставку річного проценту, %: "))

after_one_year = deposit + deposit*interest/100

print(f"Наприкінці року сума вашого влкаду з відсотками складатиме: {after_one_year}")