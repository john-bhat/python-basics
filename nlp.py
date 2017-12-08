# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:53:53 2017

@author: admin
"""

nltk.download()
import nltk
from nltk.tokenize import word_tokenize ,sent_tokenize

ex_text=" Hello there, how are you doing great? The weather is awesome and Python is great. The sky is blue"

#sentence tokenize

print(sent_tokenize(ex_text))

#word tokenize

wt=word_tokenize(ex_text)

for w in  wt:
     print(w)

     
#stop words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

ex=" this is an example of stop words. i am going to demonstrate it ist time. what is your opinion"

stop_words=set(stopwords.words("english")) 

filter_ex=[]

for i in word_tokenize(ex):
    if i not in stop_words:
        filter_ex.append(i)
        
print(filter_ex)

words=word_tokenize(ex)
filterwrds=[w for w in  words if not w in stop_words]
print(filterwrds)


#stemming


st_ex="varied loving it is going to helareously possibly awkwardly cowardly during operation eating bathing in sunlight"

from nltk.stem import PorterStemmer

ps=PorterStemmer()  
words=word_tokenize(st_ex)

ps_wrds=[ps.stem(w) for w in words]
print(ps_wrds)





#parts of speech tagging

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

trtxt=("this is beauetih v lsjbfhpsi MR. Obama is very tall where as Hillary is hilarious")

import os
os.chdir("C:/Users/admin/Desktop/python")

train1=state_union.raw("C:/Users/admin/Desktop/python/test.txt")

f=PunktSentenceTokenizer(train1)

j=f.tokenize(train1)
wrds=[]
for i in j:
    wrds=nltk.word_tokenize(i)
    tagg=nltk.pos_tag(wrds)
    print(tagg)

#chunking


train1=state_union.raw("C:/Users/admin/Desktop/python/test.txt")

f=PunktSentenceTokenizer(train1)

j=f.tokenize(train1)
wrds=[]
for i in j:
    wrds=nltk.word_tokenize(i)
    tagg=nltk.pos_tag(wrds)
    chunkgram= r"""Chunk:{<RB.?>*<VB.?>*<NNP><NN>?}"""
    chunkparser=nltk.RegexpParser(chunkgram)                      
    chunked=chunkparser.parse(tagg)
    print(chunked)
    
chunked.draw()    
    



#chinking removal of something from chunk

train1=state_union.raw("C:/Users/admin/Desktop/python/test.txt")

f=PunktSentenceTokenizer(train1)

j=f.tokenize(train1)
wrds=[]
for i in j[5:]:
    wrds=nltk.word_tokenize(i)
    tagg=nltk.pos_tag(wrds)
    chunkgram= r"""Chunk:{<.*>+}
                        }<VB.?|IN|DT|TO>+{"""
    chunkparser=nltk.RegexpParser(chunkgram)                      
    chunked=chunkparser.parse(tagg,binary=True)
    print(chunked)
    
chunked.draw()    



#Lemmatizer : similar to stem but output is original word or similar to the original word with same meaning
from nltk.stem  import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

print(lemmatizer.lemmatize("loving"))
print(lemmatizer.lemmatize("loving","v"))
print(lemmatizer.lemmatize("has"))


print(lemmatizer.lemmatize("jogging"))

print(lemmatizer.lemmatize("geese"))

print(lemmatizer.lemmatize("kisses"))
print(lemmatizer.lemmatize("loves"))

#it takes only plural and converts into singular
print(lemmatizer.lemmatize("better",pos="a"))
#it changes adjective
#default is noun

print(lemmatizer.lemmatize("bitter"))


###############################
print(nltk.__file__)



#getting data from nltk corpus

from nltk.corpus import product_reviews_1

from nltk.tokenize import sent_tokenize

sample=product_reviews_1.raw("Nokia_6610.txt")

tok=sent_tokenize(sample)

print(tok[1:5])

#######################################


# word_tokenize
import nltk
from nltk.tokenize import word_tokenize
s = '''Good muffins cost $3. 8s\nin NewYork.  Please buy me two of them.\n\nThanks.'''
print("Sentence: \n\n"+s) 
print("\nword_tokenize output")
print(word_tokenize(s))
print("\n")


# word_tokenize
import nltk
from nltk.tokenize import wordpunct_tokenize
s = '''Good muffins cost $3.88\nin New.York.  Please buy me two of them.\n\nThanks.'''
print("Sentence: \n\n"+s) 
print("\wordpunct_tokenize output")
print(wordpunct_tokenize(s))
print("\n")


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
s1 = '''Good muffins cost $3.88\n to co-author in New York.  Please buy me two of them.\n\nThanks.'''
s2= "abc is the context-based approach for morph-analysis\n. The accuracy of the approach is 77.80%"
print("Sentence: \n\n"+s2) 
print("\nsent_tokenize(s) output")
print(sent_tokenize(s2))
print("\n")


## Tokenization using NLTK

# LineTokenizer
import nltk
from nltk.tokenize import LineTokenizer


s = "I love kites\rI like cricket\n I like football\n"

print("Sentence: "+s) 
print("LineTokenizer...")
print(LineTokenizer().tokenize(s))
print("\nWords in a sentence: ")
for sent in LineTokenizer().tokenize(s):
    print word_tokenize(sent)
    
    
    
    
# RegexpTokenizer
from nltk.tokenize import RegexpTokenizer


    

s = "Petrol price has gone upto Rs.75.89. 01-02-2015 I,John and Mrs. Thomas are thinking of using electric scooters."
tokenizer = RegexpTokenizer('Rs\.[\d\.]+|\w+|\S+')
print("Sentence: "+s)
print("\nRegexpTokenizer...")
print(tokenizer.tokenize(s))
print("\n")




###extract date 
tokenizer = RegexpTokenizer('\d{1-31}[^A-Z0-9]*\d{1-12}[^A-Z0-9]*\d{4}')
print("Sentence: "+s)
print("\nRegexpTokenizer...")
print(tokenizer.tokenize(s))
print("\n")
#Let us say we want to extract all words beginning with an uppercase character
capword_tokenizer = RegexpTokenizer('[A-Z]\w+\S+')
print(capword_tokenizer.tokenize(s))



from nltk.tokenize import SExprTokenizer
s = '(a(b c)d)ef(g(h(i)))'
print("Sentence: "+s)
print("\nSExprTokenizer...")
print(SExprTokenizer().tokenize(s))
print("\n")








#TreebankWordTokenizer
from nltk.tokenize import TreebankWordTokenizer




s = "Petrol price has gone upto Rs.75.89. I,John and Mrs. Thomas are thinking of using electric scooters."
print("Sentence: "+s)
print("\nTreebankWordTokenizer...")
print(TreebankWordTokenizer().tokenize(s))
print("\n")

s = "@someone did you check out this #superawesome!! it's very cool \xF0\x9F\x98\x81 http://t.co/ydfY2"
print("Sentence: "+s)
print(TreebankWordTokenizer().tokenize(s))
print("\n")

s = "@Nike's quest to break the 2-hour marathon barrier is LIVE on Twitter. #Breaking2"
print("\nSentence: "+s)
print(TreebankWordTokenizer().tokenize(s))


from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
s0 = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"
tknzr.tokenize(s0)




tweet = str("@someone did you check out this #superawesome!! it's very cool \xF0\x9F\x98\x81 http://t.co/ydfY2")
# print(tknzr.tokenize(tweet))

s = str("@Nike's quest to break the 2-hour marathon barrier is LIVE on Twitter. #Breaking2")
#tknzr.tokenize(s)


