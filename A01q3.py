takeInput = input("Enter the Sample String : ") # input sample string 
newStr = takeInput.replace(" ","") # removing spaces so that it would be One String
if newStr.isalnum():  # to check string should have (a-z) or (0-9)
    print("String is Accepted")
else : 
    print("String is not Accepted")