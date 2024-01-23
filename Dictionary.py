#"Create a script that prompts for a number and creates a dictionary where the keys range from 1 to the specified number, and the values are the squares of the keys."

number = int(input("Enter a number: "))
squares = {}

for num in range(1, number + 1):
    squares[num] = num ** 2

for num, value in squares.items():
    print("%d -> %d" % (num, value))
