
distance = int(input())
age = int(input())

fare = distance * 2

if age >= 60:
    fare = fare * 0.70
elif age < 12:
    fare = fare * 0.50

print(int(fare))