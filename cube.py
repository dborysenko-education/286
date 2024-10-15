rebro = float(input("Введіть довжину ребра куба, см: "))
if int(rebro) == 0: 
    exit("Несподіване значення")

rebro_txt = str(rebro)
if str(rebro_txt[0]) == "-": 
    exit("Несподіване значення")

v = rebro ** 3
s = rebro ** 2 * 6
print(f"Об'єм куба зі стороною {rebro} = {round(v, 2)} кубічних сантиметрів. \nПлоща поверхні куба зі стороною {rebro} = {round(s, 2)} квадратних сантиметрів")