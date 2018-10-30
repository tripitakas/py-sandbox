def Cal_Rep(Text,word):
    'calculate the repetition number of word in Text'
    number = 0
    for t in Text:
            if t == word:
              number += 1
    return number

def Cal_Len(Text):
    'calculate the length of Text'
    number = 0
    for t in Text:
        number += 1
    return number

Text = input('please input a text:')
print(Cal_Len(Text))
word = input('please input a word:')
print(Cal_Rep(Text,word))
