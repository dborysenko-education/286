daryna = float(input("Enter Daryna's weight, kg: "))
natalka = daryna + 5
candies = float(input("Enter weight of candies, kg: "))

if candies <= daryna + natalka: 
    exit("More candies!!!11111")

diff = candies - (natalka + daryna)

print(f"Natalka and Daryna have to eat {diff} kg of candies!")