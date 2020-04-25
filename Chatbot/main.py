# -*- coding: utf-8 -*-


import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer=LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json

with open("intents.json") as file:
    data=json.load(file)
    
words=[]
labels=[]
docs_x=[]
docs_y=[]

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds= nltk.word_tokenize(pattern)
        print(wrds)
              
        
        

    

