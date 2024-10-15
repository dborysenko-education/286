deposit = int(input("Введіть сумму, яку кладете на депозит: "))
interest = int(input("Введіть ставку річного проценту, %: "))/100
years = int(input("На скільки років влкадаєте гроші під простий процент: "))
after_all_years = deposit + years*deposit*interest/100
monthly_interest = interest / 12

for year in range(0, years): 
    for month in range(0, 12): 
        earned = deposit * monthly_interest
        deposit += earned
        print(f"Сума депозиту на місяць: {month+1} року: {year+1} складає: {deposit}")




print(f"Наприкінці терміну сума вашого влкаду по простому відстку складатиме: {after_all_years}")
print(f"Наприкінці терміну сума вашого влкаду по складному відсотку складатиме: {deposit}")
print(f"Вигода влкаду по складному відсотку: {deposit - after_all_years}")