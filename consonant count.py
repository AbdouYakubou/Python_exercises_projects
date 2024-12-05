vowels = "aeiou"

user_input = input("enter a word to count").lower()

consonant_count = 0

for char in user_input:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
print(consonant_count)