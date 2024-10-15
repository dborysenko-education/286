text = input("Введіть декілька речень: ")
# print("With WHILE: ", end="") 
# i = 0 
# text_volume = len(text)
# while i < text_volume: 
#     char = text[i]
#     if char == ".": 
#         break
#     print(char, end="")
#     i += 1
# print("\nWith FOR: ", end="") 
# for symbol in text: 
#     if symbol == ".": 
#         break
#     print(symbol, end="")
# print("\nWith SPLIT(): ", end="") 
# senteces = text.split(".")
# print(senteces[0])

# sentences_count = 0 
# for symbol in text: 
#     if symbol == ".": 
#         sentences_count += 1
#     elif symbol == "!":
#         sentences_count += 1
#     elif symbol == "?":
#         sentences_count += 1
# print(f"Sententces count: {sentences_count}")

# dots = 0
# q_marks = 0
# e_marks = 0
# for symbol in text: 
#     if symbol == ".": 
#         dots += 1
#     elif symbol == "!":
#         e_marks += 1
#     elif symbol == "?":
#         q_marks += 1

# print(f"Dots: {dots}")
# print(f"Exclamation marks: {e_marks}")
# print(f"Question marks: {q_marks}")
sentences = 0
for char in [".", "!", "?"]: 
    count = text.split(char)
    sentences += len(count)-1
print(f"Sententces count: {sentences}")
