#this program  searches a file for anagrams of a given word, printing the results in alphabetical order
#Busisiwe Michelle Ndlovu
#30/4/2023
import os
if os.path.isfile("EnglishWords.txt"):
    print("***** Anagram Finder *****")
    #user inputted word to be checked
    userin = input("Enter a word:\n")
    userin = userin.lower()

    #creates a dictionary to store each letter of the inputted word
    letters = {}
    #adds each letter to the dictionary and the amount of occurences
    for letter in userin:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1

    #opens words file
    words = open('EnglishWords.txt','r')
    file = words.read()

    #finds index of start of words after "START"
    startindex = (file.find("START")+6)
    file = file[startindex:]
    #replaces new lines with spaces
    file = file.replace("\n"," ")
    #array to store words that match the given criteria 
    matches = []
    #splits words by new lines with spaces
    file = file.split(' ')
    #creates dictionary for words in file
    for word in file:
        letterscheck = {}
        for letter in word:
            if letter not in letterscheck:
                letterscheck[letter] = 1
            else:
                letterscheck[letter] += 1
        if letters == letterscheck and word != userin:
            matches.append(word)
    #if there are not matches
    if len(matches) ==  0:
        print(f"Sorry, anagrams of '{userin}' could not be found.")
    else:
        matches.sort()
        print(matches)
else:
    print("***** Anagram Finder *****")
    print("Sorry, could not find file 'EnglishWords.txt'.")
