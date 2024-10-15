deposit = int(input("Введіть суму депозиту: "))
interest = int(input("Введіть річну процентну ставку, %: "))/100
years = int(input("Введіть кількість років: "))
end_of_period = deposit + deposit*interest*years
depo_for_compound = deposit
monthly_interest = interest/12
for year in range(years): 
    for month in range(12): 
        depo_for_compound += depo_for_compound*monthly_interest
        print(f"Станом на місяць №{month+1} року №{year+1} - стан депозиту: {depo_for_compound}")
print(f"На кінець періода в {years} років, по простому відсотку: {end_of_period}")
print(f"На кінець періода в {years} років, по складному відсотку: {depo_for_compound}")
print(f"Вигода на кінець періода в {years} років, по складному відсотку: {depo_for_compound - end_of_period}")

