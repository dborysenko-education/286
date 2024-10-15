text = input("Введіть декілька речень: ")
# print("With While: ", end="")
# i = 0
# text_volume = len(text)
# while i < text_volume: 
#     char = text[i]
#     if char == ".":
#         break
#     print(char, end="")
#     i += 1


# print("\nWith For: ", end="")
# for letter in text: 
#     if letter == ".":
#         break
#     print(letter, end="")

# print("\nWith .split(): ", end="")
# sentences = text.split(".")
# print(sentences[0])


sentences = 0
for char in text: 
    if char == ".":
        sentences += 1
    elif char == "!":
        sentences += 1
    elif char == "?":
        sentences += 1
print(f"Sentences count with FOR: {sentences}")

sentences_2 = 0
for char in ["!", "?", "."]: 
    division = text.split(char)
    sentences_2 += len(division)-1
print(f"Sentences count with SPLIT: {sentences_2}")



