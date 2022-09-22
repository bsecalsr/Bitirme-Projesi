import nltk 
from nltk.tokenize import word_tokenize 

file = open("kmm.txt",newline='', encoding='utf-8')
result = file.read()
words = word_tokenize(result)
#for i in words:
 #      metin = i 
       
dosya = open("deneme1.txt", "w")
dosya.write( '\n'.join(words) )
dosya.close()


       
