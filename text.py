text = input("Введіть декілька речень: ")

# i = 0 
# text_2 = ""
# while True: 
#     if text[i] == ".":
#         break
#     text_2 += text[i]
#     i += 1
# print(text_2)

# text_3 = ""
# for letter in text: 
#     if letter == ".":
#         break
#     text_3 += letter
# print(text_3)

sentences = text.split(".")
print(sentences[0])
print(len(sentences))

sentences_2 = 0
for char in text: 
    if char == ".": 
        sentences_2 += 1
    elif char == "!" :
        sentences_2 += 1
    elif char == "?":
        sentences_2 += 1
        
print(sentences_2)