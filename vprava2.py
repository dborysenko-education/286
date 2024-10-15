initial_words = ["школа", "книга", "голуб", "зошит", "аркуш"]
initial_results = ["шшккооллаа", "нкгиа", "гбоблбубб", "10791086109610801090", "бслфщ"]

words = ["школа", "книга", "голуб", "зошит", "аркуш"]
results = []

w_1 = words[0]
w_2 = words[1]
w_3 = words[2]
w_4 = words[3]
w_5 = words[4]

# def result(func): 
#     def wrapper(): 
#         results.append(func())

r_1 = ""
r_2 = ""
r_3 = ""
r_4 = ""
r_5 = ""

# 1 
for letter in w_1: 
    r_1 += letter *2
results.append(r_1)

# 2 
w_2_pairs = []
for i in range(0, len(w_2), 2): 
    pair = w_2[i:i+2] # w_2[0:2]
    w_2_pairs.append(pair[::-1])
r_2 = "".join(w_2_pairs)
results.append(r_2)

# 3
last_letter_index = len(w_3)-1
for letter in w_3: 
    r_3 += letter + w_3[last_letter_index]
results.append(r_3)

# 4 
for letter in w_4: 
    r_4 += str(ord(letter)) 
results.append(r_4)

# 5
w_5_letter_codes = []
for letter in w_5: 
    w_5_letter_codes.append(ord(letter)+1)

for code in w_5_letter_codes: 
    r_5 += chr(code)
results.append(r_5)

    
if len(results) != len(words): 
    print("Less results than words")
else: 
    for i, result in enumerate(results): 
        print(f"{words[i]} -> {result}") 

if words == initial_words: 
    for i, result in enumerate(results): 
        print(f"task #{i}:  word: {words[i]} resulted in {result}; initial result: {initial_results[i]}")
        if result == initial_results[i]:
            print(f"status: OK ")
        else: 
            print(f"status: FAIL ")