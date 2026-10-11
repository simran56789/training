
password = input()

digit = False
uppercase = False

for ch in password:
    if ch.isdigit():
        digit = True
    if ch.isupper():
        uppercase = True

if len(password) >= 8 and digit and uppercase:
    print("STRONG")
else:
    print("WEAK")