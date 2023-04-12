import random

numbers = []

# loop until we have 1000 unique 3-digit numbers
while len(numbers) < 100:
    # generate a random 3-digit number
    num = random.randint(100, 999)
    # check if the digits are unique
    if len(set(str(num))) == 3:
        # add the number to the list
        numbers.append(num)

print(numbers)