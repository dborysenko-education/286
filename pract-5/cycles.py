number = int(input("Enter a number: "))

divider = 1
possible_dividers = range(divider, number+1)

dividers = []
n_dividers = 0 

for d in possible_dividers: 
    if number % d == 0: 
        n_dividers += 1
        dividers.append(d)

if n_dividers == 2: 
    print(f"Число {number} - просте. Дільників: {n_dividers}, дільники: {dividers}")
elif n_dividers > 2: 
    print(f"Число {number} - НЕ просте. Дільників: {n_dividers}, дільники: {dividers}")
elif n_dividers == 1: 
    print(f"Число {number} - 1")
else: 
    print(f"Неправильне / невідоме число")