text=input("Please insert a text of your choice: ")
text=text.lower()

ask1=input("Please insert 1 letters of your choosing: ")
ask2=input("Please insert 1 letters of your choosing: ")
ask3=input("Please insert 1 letters of your choosing: ")
ask1=ask1.lower() 
ask2=ask2.lower() 
ask3=ask3.lower() 
    
print(f"this is how many times your first letter was in the text: {(text.count(ask1))}")
print(f"this is how many times your second letter was in the text:{(text.count(ask2))}")
print(f"this is how many times your third letter was in the text: {(text.count(ask3))}")



texts=(text.split(" "))
print(f"The number of words in your text is {len(texts)} words")
print(f"this is the first letter of your text:{text[0]}")
print(f"this is the last letter of your text:{(text[-1])}")

print(f"this is your text backwords: {text[::-1]}")

p='python'
if p in text:
    print(f'{p} is present in the text')
else:
    print(f'{p} is not present in the text')

