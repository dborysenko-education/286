from math import pi 

dov = int(input("Введіть довжину: "))
shyr = int(input("Введіть ширину: "))
ploshcha = dov * shyr
kvity =  ploshcha * 4
parkan = (dov + shyr) * 2 

print(f"Для клумби площею {ploshcha} м.кв, потрібно закупити стільки саджанців: {kvity}, і стільки метрів огорожі: {parkan}")