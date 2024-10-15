number = int(input("Input a number: "))

numbers = range(1, number+1)
s = 0
for n in numbers: 
    s += n 
    print(n)
print(s)

n1 = 0
s1 = 0
while n1 <= number: 
    s1 += n1
    n1 += 1
    print(n1)
print(s1)