# You can remove 'pass' if you written code in the function 

# Exercise 1
def count_characters(text):
    return len(text)


# Exercise 2
def remove_spaces(text):
    return text.replace(" ", "")


# Exercise 3
def count_vowels(text):
    return sum(text.lower().count(vowel) for vowel in "aeiou")


# Exercise 4
def replace_vowels(text):
    result = ""
    for char in text:
        if char in "aeiouAEIOU":
            result += "*"
        else:
            result += char
    return result


# Exercise 5
def count_words(text):
    words = text.split()
    return len(words)


# Exercise 6
def find_longest_word(text):
    words = text.split()
    return max(words, key=len) if words else ""
