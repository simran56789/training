
amount = float(input())

if amount >= 5000:
    discount = 0.20
elif amount >= 3000:
    discount = 0.10
elif amount >= 1000:
    discount = 0.05
else:
    discount = 0

payable = amount - amount * discount

print(int(payable) if payable.is_integer() else payable)