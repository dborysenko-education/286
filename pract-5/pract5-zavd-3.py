# Завдання. У програмі Розрядні одиниці вводять чотиризначне ціле число 
# й отримують запис числа у вигляді суми розрядних одиниць. 
# Наприклад, для введеного числа 5843 отримують 
# 5*1000+8*100+4*10+3*1

integer = input("Введіть чотиризначне число: ")

# визначаємо позитивне чи негативне число ввів користувач
negative = False
if integer[0] == "-":
    integer = integer[1:]
    negative = True

# відфільтровуємо все, що не є виключно цілочисленними значеннями
if integer.isdigit() == False:
    exit("Only numbers are accepted!")

# прибраємо всі 0 на початку числа: 
zeroes = 0
for i in range(0, len(integer)): 
    if integer[i] == "0": 
        zeroes += 1

if len(integer) == zeroes: 
    exit("you entered only zeroes")

while "0" in integer[0]:
    integer = integer[1:]

len_int = len(integer) # кількістсь символів 

if len_int != 4: 
    exit(f"Only 4-digit integers accepted, your integer has {len_int} digits!")

chars_number = range(0, len_int)

# визначаємо кількість дільників та кожен окремий дільник
dividers = [] 
for i in chars_number: 
    divider = "1" + "0" * i # визнначаємо "розряд" кожного дільника 
    dividers.insert(0, divider) # записуємо в масив всі дільники (автоматично записується від 1 до найбільшого )

results = []
for k in chars_number: 

    if negative == True: 
        result = f"((-{integer[k]})*{dividers[k]})"
        minus = "-"
    else: 
        result = f"{integer[k]}*{dividers[k]}"
        minus = ""

    results.append(result)

beautiful_result = ' + '.join(results)

print(f"{minus}{integer} => {beautiful_result}")
