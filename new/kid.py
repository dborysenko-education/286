# за перший день - 1 рівень 
# кожнен наступний день — на три рівні більше 
# за скільки днів хлопчик дійде до 150-го рівня

target_level = 150
level = 1
days = 1
while True: 
    if level > target_level: 
        break
    level += 3
    days += 1
    print(f"Day: {days}, level: {level}")

print(f"To reach this level ({target_level}), the kid needed this amount of days: {days}")