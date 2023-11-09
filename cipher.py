# add your code here
sentence = input("Please enter your sentence:").lower().strip()
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 5
result = ""
for letter in sentence:
    if not letter.isalpha():
        result += letter
        continue
    
    index = alphabet.find(letter)
    result += alphabet[(index + shift)%26]
print("The encrypted sentence is:", result)
   