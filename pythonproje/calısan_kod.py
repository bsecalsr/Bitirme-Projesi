from zeyrek import MorphAnalyzer
import nltk
nltk.download('punkt')
from tkinter import *
from tkinter import filedialog
import pandas as pd
import re
from textblob import TextBlob
from yandex.Translater import Translater
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from TurkishStemmer import TurkishStemmer
from nltk.tokenize import word_tokenize


def stemmer(text):
   ps = TurkishStemmer()

   words = word_tokenize(text)
  
   for w in words:
      
      print(w, " : ", ps.stem(w))
      
      
      

def lemmatize(text):
    
    analyzer = MorphAnalyzer()
    result = analyzer.analyze(text)
    words = word_tokenize(text)
  
    for word in words:
      
       print(word, " : ",analyzer.lemmatize(word))







def KucukHarf(text):
     kucukcevir =  text.lower()
     return kucukcevir






def stopWords(text):
    
    words = word_tokenize(text)
    wordsFiltered = []
    
    stopWords = stopwords.words('turkish')
    stopWords.append('fakat') 
    stopWords.append('INTRODUCTION')
    
    new_words=('nın','nin', 'te', 'ta', 'sı', 'si', 'den', 'dan', 'un','ün','ın','in','de','da')
    for word in new_words:
        
        stopWords.append(word)
    
    
 
        tokens_without_sw = [word for word in words if not word in stopWords]
    
    return str(tokens_without_sw ) 

     
def noktalamaSil(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~’“”©'''
    pattern = r'[0-9]'
   
    
    no_punct = ""
    for char in text:
      if char not in punctuations:
          no_punct = no_punct + char
          new_string = re.sub(pattern, ' ',no_punct)

 
    return new_string

def bosluk_kaldır(text):
    
   bosluk =  re.sub(' +', ' ', text)
   
   return bosluk

def kökü_olmayan_kelimeler(text):
    
    shortword = re.compile(r'\W*\b\w{1,3}\b')
    return shortword.sub('', text)


def fonk_cagır(text):
    
    text = KucukHarf(text)
    text = stopWords(text)
    text = noktalamaSil(text)
    text = kökü_olmayan_kelimeler(text)
    text = bosluk_kaldır(text)
   
   # text = stemmer(text)
    text = lemmatize(text) 
    return (text)



def run_examples():
    analyzer = MorphAnalyzer()
    
    with open('giris_1.txt') as text_file:
        text = text_file.read()
    text_tokens = word_tokenize(text)
    
   # fonk_cagır_text = fonk_cagır(text)
  #  print(fonk_cagır_text)
    print(fonk_cagır(text))
  
if __name__ == '__main__':
    run_examples()
    
   


