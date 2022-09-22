import pandas as pd
import numpy as np
import pickle
from zeyrek import MorphAnalyzer
import nltk



df_old = pd.read_csv('bilgiler.txt',encoding='utf-8', error_bad_lines=False)

df_old.head()

def run_examples():
    analyzer = MorphAnalyzer()

    with open('bilgiler.txt', encoding='utf-8') as text_file:
        text = text_file.read()

    # Analyze text from the file and print out formatted parses of each word.
    result = analyzer.analyze(text)
    for word_result in result:
        print(word_result)
        for parse in word_result:
            print(parse.formatted)
        print()

def is_valid(kelime,kok):
    ret = True
    try:
        if kelime.isupper() or kok.isupper():
            print ("islower")
            ret = False
        elif not kelime.isalpha() and kelime.isalnum():
            print ("kelime digits")
            ret = False
        elif not kok.replace(':','').isalpha() and kok.replace(':','').isalnum():
            print ("kelime digits")
            ret = False
    except:
        ret = False
    return ret

sozluk = {}
def get_data(df,sozluk):
    for i in range(len(df)):
        kelime = df.kelime[i]
        kok = df.kok[i]
        if is_valid(kelime,kok):       
            if 'sozluk' in kelime:
                if kok != sozluk[kelime]:
                    print (u'Input : {} {} {} is already aded as {}'.format(i,kelime,kok,sozluk[kelime]))
            else:
                sozluk[kelime] = kok
        else:
            print (u'Input : {} {} {} not Valid '.format(i,kelime,kok))
            
    return sozluk

sozluk = get_data(df_old,sozluk)
len(sozluk)


df_out = pd.DataFrame()
df_out['kelime'] = sozluk.keys()
df_out['kok'] = sozluk.values()


df_out.to_csv('giris5.csv',encoding='utf-8',index=False)

fp = open('datafile.pkl','rb')
data = pickle.load(fp)
fp.close()

new_maxlen = max([len(x) for x in df_out.kelime ])
if data['maxlen'] < new_maxlen:
    data['maxlen'] = new_maxlen
    print ('New maxlen : ',new_maxlen    )
    fp = open('datafile.pkl','wb')
    pickle.dump(data,fp)
    fp.close()    
    print ('datafile.pkl updated')


   
if __name__ == '__main__':
    run_examples()    