# группа з 46 туристів поїхала в похід на 10 човнах 
# є човни на 4 місць
# є човни 6 місць 
# скільки човнів кожного виду

tourists = 46
boats = 10
seats_in_six_seaters = 6
seats_in_four_seaters = 4

# print(f"{tourists // six_seaters}") результат цілочисленного ділення 
# print(f"{tourists % six_seaters}") результат цілочисленного ділення
for boat in range(boats): 
    six_seater_boats = tourists // six_seaters
    passegers_left = tourists % six_seaters
    four_seater_boats = passegers_left / four_seaters
    if six_seater_boats + four_seater_boats == 10: 
        break

print(f"6-seater boats: {six_seater_boats}, 4-seater boats: {four_seater_boats}")
