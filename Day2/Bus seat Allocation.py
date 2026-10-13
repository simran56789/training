
n = int(input())
remaining = 40

for i in range(n):
    request = int(input())

    if request <= remaining:
        print("CONFIRMED")
        remaining -= request
    else:
        print("WAITLISTED")