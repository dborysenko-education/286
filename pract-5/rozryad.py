chyslo = input("Введіть чотиризначне ціле число: ")
negative = False
if chyslo[0] == "-":
    chyslo = chyslo[1:]
    negative = True
if chyslo.isdigit() == False:
    exit("Only numbers are accepted!")
zeroes = 0
for i in range(0, len(chyslo)): 
    if chyslo[i] == "0": 
        zeroes += 1
if len(chyslo) == zeroes: 
    exit("you entered only zeroes")
while "0" in chyslo[0]:
    chyslo = chyslo[1:]
len_int = len(chyslo) # кількістсь символів 
if len_int != 4: 
    exit(f"Only 4-digit chyslos accepted, your chyslo has {len_int} digits!")
chars_number = range(0, len_int)
dividers = [] 
for divider in chars_number: 
    divider = "1" + "0" * divider # визнначаємо "розряд" кожного дільника
    dividers.insert(0, divider) # записуємо в масив всі дільники (автоматично записується від 1 до найбільшого )
results = []
for i in chars_number: 
    if negative == True: 
        result = f"(-{chyslo[i]})*{dividers[i]}"
        minus = "-"
    else: 
        result = f"{chyslo[i]}*{dividers[i]}"
        minus = ""
    results.append(result)
beautiful_result = ' + '.join(results)
print(f"{minus}{chyslo} => {beautiful_result}")