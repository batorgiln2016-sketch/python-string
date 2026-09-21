# You can remove 'pass' if you written code in the function 

# Exercise 1
def count_characters(text):
    print(len(text))


# Exercise 2
def remove_spaces(text):
    print(text.replace(" ", ""))


# Exercise 3
def count_vowels(text):
    print(sum(text.lower().count(vowel) for vowel in "aeiou"))


# Exercise 4
def replace_vowels(text):
    vowels = "aeiouAEIOU"
    print("".join("*" if char in vowels else char for char in text))


# Exercise 5
def count_words(text):
    words = text.split()
    print(len(words))


# Exercise 6
def find_longest_word(text):
    words = text.split()
    print(max(words, key=len) if words else "")
