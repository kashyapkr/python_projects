#Remove punctuations from a string
'''import string
pun = string.punctuation
str= "Wow!!! we are going ahead with our course --/. aren't you excited/)"
new_str = str
for char in str:
    if char in pun:
        new_str = new_str.replace(char,"")
print(new_str)'''

#Remove punctuations from a text file
'''import string
with open ("info","r") as f:
    text = f.read()
    words = text.split()
    table = str.maketrans("","",string.punctuation)

    stripped = [ a.translate(table) for a in words]
    assemble = " ".join(stripped)
    print(assemble)'''




