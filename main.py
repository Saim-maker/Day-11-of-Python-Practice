# Nested Loops : A Loop within another loop is called nested loop
#               outer loop:
#                    inner loop:

for x in range(3):
    for y in range(0,10):
        print(y,end = " ")
    print()

rows = int(input("Enter the number of row: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter symbol: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()

rows = int(input("Enter the number of row: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter symbol: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()