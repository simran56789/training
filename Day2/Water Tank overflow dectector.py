
n = int(input())
inflows = list(map(int, input().split()))

water = 0

for i in range(n):
    water += inflows[i]

    if water > 1000:
        print(i + 1)
        break