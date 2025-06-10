num0fWords = 0
num0fLetters = 0
num0fDigits = 0

text = input("Enter a text of numbers : ")# My name is 123

for x in text:
    x= x.lower()
    if x>='a' and x<='z':
        num0fLetters=num0fLetters+1
    elif x>='0' and x<='9':
        num0fDigits=num0fDigits+1
    elif x=='':
        num0fWords=num0fWords+1

print("Number of Letters : ",num0fLetters)
print("Number of Digits : ",num0fDigits)
print("Number of Words : ",num0fWords+1)            
