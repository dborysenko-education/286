deposit = int(input("Введіть суму депозиту: "))
interest = int(input("Введіть річну ставку: "))/100
years = int(input("Введіть кількість років: "))
end_of_period = deposit + deposit*interest*years
monthly_interest = interest / 12
deposit_for_compound = deposit
for year in range(years): 
    for month in range(12): 
        deposit_for_compound += deposit_for_compound * monthly_interest
        print(f"На місяць №{month+1} року № {year+1} - сума депозиту = {deposit_for_compound}")
print(f"Через стільки років ({years}) ви отримаєте стільки грошей -- {end_of_period} по простому відсотку. ")
print(f"Через стільки років ({years}) ви отримаєте стільки грошей -- {deposit_for_compound} по складному відсотку. ")
print(f"Вигода від складного відсотка: {deposit_for_compound - end_of_period}  ")
