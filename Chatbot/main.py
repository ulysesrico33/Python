# -*- coding: utf-8 -*-


import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer=LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json


try:
    with open("intents.json") as file:
        data=json.load(file)
        
    words=[]
    labels=[]
    docs_x=[]
    docs_y=[]
    print('OK...')

except e:
    print('Error:'+e)
              
        
        

    

