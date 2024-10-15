# професійні ваги можуть зважити 1000 кг
# ваги навантажуються коробками 
# вагу кожної коробки вводить користувач
# скільки коробок буде на вагах, коли пролунає сигнал перевищення

max_weight = 1000
boxes = 0 
weight = 0 
while weight < max_weight: 
    weight += int(input("Input Box Weight: "))
    boxes += 1
print(f"This amount of boxes weights more than {max_weight}: {boxes}. ")