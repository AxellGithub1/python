string = input("Enter your numbers: ")
array = string.split()
numbers = [int(x) for x in array]
even = 0
suma = 0
for i in numbers:
    suma += i
    if i % 2 == 0:
        even += 1

print("Sum: " + str(suma) + "\nMin: " + str(min(numbers)) + "\nMax: " + str(max(numbers)) + "\nEven numbers: " + str(even))