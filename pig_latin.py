#program that takes a sentence and translates it to a Pig Latin Variant
#Busisiwe Michelle Ndlovu
#27/3/23

#lowers the case of the sentnece
sentence = (input("Enter a sentence:\n")).lower()
                
                
count = 0
ans =""
#splits sentence into differnet words
words = sentence.split()

for word in words:
    #checks if the first letter of each word is a vowel
    if word[0] in "aeiou":
        #adds way
        print( word + "way", end = " ")
    else:
        #variable to store consonants in cases of non vowel start
        consonants = ''
        i = 0
        #as long as the lette risnt a cowel these alues are added to the consonant
        while i < len(word) and word[i] not in "aeiou":
            consonants += word[i]
            i += 1
        word = word[i:] + "a"+ consonants + 'ay'
        print(word, end = " ")


