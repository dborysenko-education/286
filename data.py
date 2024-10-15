# первинні дані: 
data = [
    [-86.206204752, 34.260206472, 1, 'Albertville Middle School', 10000500870, 259, 87, '2020-2021', 34.2602, -86.2062],
    [-86.2049047519999, 34.262206474, 2, 'Albertville High School', 10000500871, 261, 92, '2020-2021', 34.2622, -86.2049],
    [-86.2201047569999, 34.273306475, 3, 'Albertville Intermediate School', 10000500879, 139, 61, '2020-2021', 34.2733, -86.2201],
    [-86.221810756, 34.2527064710001, 4, 'Albertville Elementary School', 10000500889, 227, 110, '2020-2021', 34.2527, -86.221806],
    [-86.193304751, 34.289806479, 5, 'Albertville Kindergarten and PreK', 10000501616, 373, 124, '2020-2021', 34.2898, -86.1933],
    [-86.221804757, 34.253306471, 6, 'Albertville Primary School', 10000502150, 224, 109, '2020-2021', 34.2533, -86.2218],
    [-86.2541047829999, 34.533706528, 7, 'Kate Duncan Smith DAR Middle', 10000600193, 296, 85, '2020-2021', 34.5337, -86.2541],
    [-86.1420047399999, 34.362506497, 8, 'Asbury High School', 10000600872, 233, 143, '2020-2021', 34.3625, -86.142],
    [-86.27040478, 34.406906501, 9, 'Claysville School', 10000600876, 243, 123, '2020-2021', 34.4069, -86.2704],
    [-86.32126378, 34.1762404500001, 10, 'Douglas Elementary School', 10000600877, 206, 44, '2020-2021', 34.176234, -86.321259]
]

# потрібні стовпці: 3, 5, 6

# створення нового набору даних: 
school_accuracy = [] 
# наповнення нового набору даних: 
for school in data: 
    # print(f"Name: {school[3]}, IPR_EST:{school[5]}, IPR_SE:{school[6]}")
    # print(f"Name: {school[3]}, ACCURACY:{round(school[5]/school[6], 3)} ")
    school_accuracy.append([school[3], round(school[5]/school[6], 3)])

# вивід нового набору даних: 
print(school_accuracy)
# що виведе: 
# [
#     ['Albertville Middle School', 2.977], 
#     ['Albertville High School', 2.837], 
#     ['Albertville Intermediate School', 2.279], 
#     ['Albertville Elementary School', 2.064], 
#     ['Albertville Kindergarten and PreK', 3.008], 
#     ['Albertville Primary School', 2.055], 
#     ['Kate Duncan Smith DAR Middle', 3.482], 
#     ['Asbury High School', 1.629], 
#     ['Claysville School', 1.976], 
#     ['Douglas Elementary School', 4.682]
# ]

# створення відсортованого набору даних:
sorted_schools = [['Albertville Middle School', 2.977]] 

# сортування даних з набору school_accuracy: 
# перевірка яке з двох чисел більше: 
    # якщо нове більше за наявне - нове йде в кінець набору, 
    # якщо навпаки - нове йде на початок набору

for index in school_accuracy: 
    if sorted_schools[0][1] > index[1]: 
        sorted_schools.insert(0, index) # додавання елементу на початок набору
    elif sorted_schools[0][1] == index[1]: 
        ...
    else: 
        sorted_schools.append(index) # додавання елементу на в кінець набору

# вивід відсортованого набору
print(sorted_schools)


# вивід відсортованого набору sorted_schools
# [['Asbury High School', 1.629], 
#  ['Albertville Primary School', 2.055], 
#  ['Albertville Elementary School', 2.064], 
#  ['Albertville Intermediate School', 2.279], 
#  ['Albertville High School', 2.837], 
#  ['Albertville Middle School', 2.977], 
#  ['Albertville Kindergarten and PreK', 3.008], 
#  ['Kate Duncan Smith DAR Middle', 3.482], 
#  ['Claysville School', 1.976], <-------- як поставити цю школу на відповідне їй місце? 
#  ['Douglas Elementary School', 4.682]]