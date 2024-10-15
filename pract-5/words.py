input_text = input("Enter some text: ")

t = "siluhgoisrtlgiwrtg.wretglkejrtlykejty.lksjhbflkgjbertnh"

# for letter in input_text: 
#     if letter == ".": 
#         break 
#     print(letter, end="")

text = input_text.split(".")

print(text[0])
print(len(text))