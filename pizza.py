number_of_pizzas = int(input("Enter the number of pizzas you are buying: "))
pizza_price = float(input("Enter the price of a single pizza: "))
total = number_of_pizzas * pizza_price
discount = 0.1 
discounted_total = total - total * discount

print(f"The billable amount of your check for {number_of_pizzas} pizzas that each costs ${pizza_price} is ${round(discounted_total, 2)}. \nIts our Birthday, enjoy your 10% discount! ")