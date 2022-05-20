takeInput = input("Enter the String : "); # take input for string or sentence
newData = takeInput.split(" ") # using spliy for make one common string (bydefault) 
newWords = ""       # for adding new string 
for words in newData:      # iterating one string at a time after split method
    if(len(words) == 1):    # if suppose string has one character for that
        newWords += words[0].upper()+ " ";   # for changing one char
    else:
        newWords += words[0].upper() + words[1:len(words)-1] + words[-1].upper() + " ";  #changing more than one character
    # print(len(words))
    
print(newWords) # prining new string