sizing_chart = [
    ('S', 18, 28, 8.13),
    ('M', 20, 29, 8.38),
    ('L', 22, 30, 8.63),
    ('XL', 24, 31, 8.88),
    ('2XL', 26, 33, 9.63),
    ('3XL', 28, 34, 10.13)
]
shirtWidth = float(input("Enter shirt width in inches: "))
shirtLength = float(input("Enter shirt length in inches: "))
shirtSleeve = float(input("Enter shirt sleeve length in inches: "))
for size, width, length, sleeve in sizing_chart:
    if shirtWidth >= width - 0.5 and shirtWidth <= width + 0.5 \
            and shirtLength >= length - 0.5 and shirtLength <= length + 0.5 \
            and shirtSleeve >= sleeve - 0.5 and shirtSleeve <= sleeve + 0.5:
        print("Your shirt size is:", size)
        break
else: print("N/A")

