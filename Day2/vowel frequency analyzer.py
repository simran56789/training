
sentence = input()
vowel_count = 0

for ch in sentence.lower():
    if ch in "aeiou":
        vowel_count += 1

print(vowel_count)