import string
text="Hello, World! How are you?"
a = text.translate(str.maketrans("", "", string.punctuation)) 
print(a) 
