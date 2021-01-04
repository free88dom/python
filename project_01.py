'''
author = Jiri Svoboda
'''

import sys

texts = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

credentials = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

delimiter = 100 * '#'

words_total = 0
capital_words = 0
uppercase_words = 0
lowercase_words = 0
numeric = 0
numeric_list = []
counts_set = set()
counts_list = []

print(delimiter,
      "Welcome to the application".center(100, " "),
      delimiter,
      sep=f"\n")

user_password_input = input(f"Please enter the name and password delimited with space....[username password]: ")

username, password = user_password_input.split(" ")  # here splitting the user input string

while username in credentials and password == credentials[username]:  # here testing, if the entered
    # username/password matches
    print(delimiter,
          "\nWe have 3 texts to be analyzed.")
    selection = int(input(f"\nEnter a number btw. 1 and 3 to select: "))

    for word in texts[selection - 1].split():  # iteration over the text with splitting
        word_stripped = word.strip("./-?")
        words_total += 1  # counting the total_words

        if word_stripped[0].isupper():
            capital_words += 1  # counting the title cased words

        elif word_stripped.isupper():
            uppercase_words += 1  # counting the upper cased words

        elif word_stripped.islower():
            lowercase_words += 1  # counting the lower cased words

        elif word_stripped.isnumeric():
            numeric += 1  # counting the numeric words
            numeric_list.append(float(word_stripped))  # creating the list with numbers to count them later on

        counts_set.add(len(word_stripped))  # with the set, i only get a unique set of different lengths
        counts_list.append(len(word_stripped))  # with the list, i can count the occurrences of the same length

    counts_length = [counts_list.count(i) for i in counts_set]  # with help of this iteration,
    # i can count the occurrences of each length

    print(f"\n{delimiter}",
          f"\nTotal number of words are: {words_total}",
          f"\nTitle cased word is {capital_words}" if capital_words <= 1 else f"\nTitle cased words are {capital_words}",
          f"\nUppercase word is {uppercase_words}" if uppercase_words <= 1 else f"\nUppercase words are {uppercase_words}",
          f"\nLowercase word is {lowercase_words}" if lowercase_words <= 1 else f"\nLowercase words are {lowercase_words}",
          f"\nNumeric is {numeric}" if numeric <= 1 else f"\nNumerics are {numeric}",
          end=f"\n{delimiter}\n")

    for num in counts_set:  # with this cycle i print the occurrences of each lengths with visualisation
        count_of_letters = counts_length.pop(0)
        print(f"{num} {'*' * count_of_letters} {count_of_letters}")

    print(f"{delimiter}",
          f"\nIf we summed all the numbers in this text we would get: {str(sum(numeric_list))}",
          end=f"\n{delimiter}")
    break

else:
    sys.exit(f"Wrong credentials")
