integer = input("input an integer: ")
# спочатку потрібно прибрати всі 0 на початку числа: 

while "0" in integer[0]:
    integer = integer[1:]

len_int = len(integer) # кількістсь символів у числі
int_chars = range(0, len_int)
# визначаємо кількість дільників та кожен окремий дільник
dividers = [] 
for divider in int_chars: 
    divider = "1" + "0" * divider # визнначаємо "розряд" кожного дільника
    dividers.append(divider) # записуємо в масив всі дільники (автоматично записується від 1 до найбільшого )
dividers = dividers[::-1] # змінюємо порядок дільникв

result = []
for i in int_chars: 
    result.append(integer[i] + "*" + dividers[i])
beautiful_result = '+'.join(result)

print(f"{integer} = {beautiful_result}")