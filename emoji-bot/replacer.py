import re
from emoji import emoji

sample = open('sample-text.txt', 'r')

doc = sample.read() 

for x in emoji:
    if x in doc:
        doc = doc.replace(x, emoji[x])  

       

print(doc)