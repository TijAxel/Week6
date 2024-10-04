text=input("Please insert a text of your choice: ")
text=text.lower()
(tuple(list(text)))
ask1=input("Please insert 1 letters of your choosing: ")
ask2=input("Please insert 1 letters of your choosing: ")
ask3=input("Please insert 1 letters of your choosing: ")
ask1=ask1.lower() 
ask2=ask2.lower() 
ask3=ask3.lower() 
    
print(f"this is how many times your first letter was in the text: {(text.count(ask1))}")
print(f"this is how many times your second letter was in the text:{(text.count(ask2))}")
print(f"this is how many times your third letter was in the text: {(text.count(ask3))}")

length=(len(text))
minus=(text.count(" "))
print(f"this is how many words are in your text: {(length) - (minus)}")




print(f"this is the last letter of your text is:{(text[-1])}")