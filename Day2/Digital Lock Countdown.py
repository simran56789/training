
number = int(input())

while number >= 10:
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    number = total

print(number)