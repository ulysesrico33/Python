# -*- coding: utf-8 -*-


import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer=LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json

with open("intent.json") as file:
    data=json.load(file)
    
print(data)    

print("So...?")
    

