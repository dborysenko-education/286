from math import pi

radius = int(input("Input radius (m): "))
ploshcha = pi * radius**2
parkan = 2 * pi * radius
sadzhantsi = round (ploshcha * 4)

print(f"Довжина огорожі = {parkan} метрів, потрібно купити стільки саджанців: {sadzhantsi}")