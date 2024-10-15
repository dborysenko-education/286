integer = input("Input a 4-digit integer here: ")
if int(integer) // 1 != int(integer): 
    print("You entered letters, please enter digits only!")

while "0" in integer[0]: 
    integer = integer[1:]
dividers = []
for divider in range(0, len(integer)): 
    divider = "1" + "0" * divider
    dividers.append(divider)
dividers = dividers[::-1]
result = []
for i in range(0, len(integer)): 
    result.append(integer[i] + "*" + dividers[i])
beautiful_result = "+".join(result)
print(f"{integer} = {beautiful_result}")