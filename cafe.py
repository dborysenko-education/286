guests = int(input("Enter amount of guests: "))
cheque = float(input("Enter cheque amount: "))
tips = float(input("Enter tips rate, %:")) / 100

grand_total = cheque + cheque * tips
portion = round(grand_total / guests, 2)

print(f"Each of {guests} guests has to pay ${portion} for a check of ${grand_total}. {tips * 100}% are included respectedly. ")