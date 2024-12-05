vowels = "aeiou"

user = input ("enter a word: ").lower()

vowels_count = 0

for char in user:
    if char in vowels: 
        vowels_count += 1
print(vowels_count)
        
    