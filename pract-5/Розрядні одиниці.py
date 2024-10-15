integer = input("Input a 4-digit integer here: ")
while "0" in integer[0]: 
    print(integer)
    integer = integer[1:]
if len(integer) > 4: 
    print("Your integer is bigger than a 4-digit number!")
    exit()
i  = integer[0] + "*1000"
i += "+" + integer[1] + "*100"
i += "+" + integer[2] + "*10" 
i += "+" + integer[3] + "*1"
print(i)