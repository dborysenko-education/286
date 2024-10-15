# word = "Python"

# letter = input("Перевірка, чи ця буква є в слові Python: ")

# if letter in word: 
#     print(f"Вдача! Буква \"{letter}\" є в слові Python! ")
# else: 
#     print(f"От халепа! Букви \"{letter}\" намає в слові Python! :( ")

# API_KEY = "CBpRWQam4It9kV1TmXCNol"

# input_api_key = input("Enter your api key: ")

# if input_api_key != API_KEY: 
#     exit("Wrong api key!")

# print("Authorization Successfull!")



# if color == "g" or color == "G": 
#     print("Green!")
# elif color == "b" or color == "B": 
#     print("Blue!")
# elif color == "w" or color == "W": 
#     print("White!")
# elif color == "y" or color == "Y": 
#     print("Yellow!")
# elif color == "p" or color == "P": 
#     print("Purple!")
# elif color == "o" or color == "O": 
#     print("Orange!")
# else: 
#     print("I don't know :(")
input_color = input("Enter first letter of a colour: ")
colors = [("bB", "Blue"), ("gG", "Green"), ("wW", "White"), 
          ("yY", "Yellow"), ("pP", "Purple"), ("oO", "Orange")]      

for i, color in enumerate(colors): 
    if input_color in color[i][0]: 
        print(color[i][1]) 