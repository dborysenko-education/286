deposit = int(input("Введіть суму депозиту: "))
interest = int(input("Введіть річну процентну ставку: "))/100
years = int(input("Введіть кількість років: "))
end_of_pediod = deposit + deposit * interest * years
monthly_interest = interest/12
depo_for_compoud = deposit
for year in range(years): 
    for month in range(12): 
        depo_for_compoud += depo_for_compoud * monthly_interest
        print(f"У місяці №{month+1} року №{year+1} стан депозиту = {depo_for_compoud}")
print(f"В кінці періода в {years} років, по простому проценту: {end_of_pediod} ")
print(f"В кінці періода в {years} років, по складному проценту: {depo_for_compoud} ")
print(f"В кінці періода в {years} років, така вигода по складному проценту: {depo_for_compoud - end_of_pediod} ")