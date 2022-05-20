takeInput = input("Enter Sample Input : ") # for sample input
count = 0 # for vowels counting by default is 0
for words in takeInput.lower(): #iterating one words but first all are lower case so exception
    for letter in words: # iterating each letter in one words

        #checking if letter is vowel or not 
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count +=1  # increment count by one if statement is true

print("Vowels : {}".format(count)); # printing vowels count