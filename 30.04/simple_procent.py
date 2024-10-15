deposit = int(input("Введіть суму депозиту: "))
interest = int(input("Введіть річну ставку, %: "))/100
years = int(input("Введіть кількість років депозиту: "))

# siple interest
end_of_period = deposit + deposit*interest*years

# compound interest
mothy_interest = interest/12
deposit_for_compound = deposit
for year in range(years): 
    for month in range(12): 
        deposit_for_compound += deposit_for_compound*mothy_interest
        print(f"Стан депозиту на місяць №{month+1} року №{year+1} -- {deposit_for_compound}")

print(f"Через стільки років ({years}) ви ви заберете такий депозит: {end_of_period} по простому відсотку. ")
print(f"Через стільки років ({years}) ви ви заберете такий депозит: {deposit_for_compound} по складному відсотку. ")
print(f"Вигода скдадного відсотку: {deposit_for_compound - end_of_period}")
