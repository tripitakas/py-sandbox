# count the number of 'a' that appear in the string name
import string


def counter(name,letter):
    # count the # of letter in name
    number = 0
    for i in name:
        if i==letter:
            number = number + 1

    return number

name = "aabcdaefa"
letter = 'a'
a = counter(name,letter)
print(a)