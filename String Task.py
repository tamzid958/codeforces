word = input()
word = word.lower()

remove_vowels = ["a", "e", "i", "o", "u", "y"]

for character in remove_vowels:
    word = word.replace(character, "")

for i in range(0, len(word)):
    print("."+word[i], end="")
