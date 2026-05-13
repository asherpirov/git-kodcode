single_char = input("enter a single char: ")

if len(single_char) != 1 or not single_char.isalpha() or not single_char.isascii():
    print("Invalid")
elif single_char.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

