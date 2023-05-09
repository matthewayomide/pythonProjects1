text = input('Enter any text of your choice: ')
letter = []
text = text.lower()

letter.append(input('Enter first random letter: ').lower())
letter.append(input('Enter second random letter: ').lower())
letter.append(input('Enter third random letter: ').lower())

print('\n') #for line breaks

print("LETTER REPETITIONS")

letter_repetetions1 = text.count(letter[0])
letter_repetetions2 = text.count(letter[1])
letter_repetetions3 = text.count(letter[2])

print(f"We have found the letter '{letter[0]}' appears {letter_repetetions1} times")
print(f"We have found the letter '{letter[1]}' appears {letter_repetetions2} times")
print(f"We have found the letter '{letter[2]}' appears {letter_repetetions3} times")


print('\n')

print('NUMBER OF WORDS IN THE TEXT')
words = text.split() # to split the text into pieces of words
print(f"There are {len(words)} number of words in your text")

print('\n')

print('THE FIRST AND LAST LETTERS')
firstLetter = text[0]
lastLetter = text[-1]
print(f"The first letter in your text is '{firstLetter}', The last Letter is '{lastLetter}'")

print('\n')

print('INVERTED TEXT')
words.reverse() #reversing the text which are splitted already to a list
inverted = " ".join(words)
print(f'The text written in a reversed other is {inverted}')

print('\n')
print("LOOKING FOR THE WORD PYTHON")
search = 'python' in text
if search:
    print('The word Python was found in your text')
else: print('The word python was not found in your text')