from __future__ import division
import operator
import re
import collections
import glob
import math
import numpy as np

books =[]

def parsetexte(file):
  f = open(file, "r")
  texte = f.read().lower()
  title = re.search(r'title: (.*)', texte)
  author = re.search(r'author: (.*)', texte)
  if not title :
    print("no title"  + file)
    return
  if not author :
    auth = "none"
  if  author :
    auth = re.sub('[^a-zA-Z]+', ' ', author.group(1))
  titl = re.sub('[^a-zA-Z]+', ' ', title.group(1))
  ponct = len(re.findall('[a-z]\.', texte))
  texte = re.sub('[^a-z]+', ' ', texte)
  mots = texte.split()
  tf = {}
  for mot in mots:
    if mot in tf:
      tf[mot]+=1 
    else:
      tf[mot]=1

  sorted_mot =  sorted(tf.items(), key=operator.itemgetter(1))
 # score = int(10*len(sorted_mot)/math.sqrt(len(mots)))
  score = int(10*len(sorted_mot)/(math.sqrt(len(mots))+math.sqrt(ponct*7)))
 
  books.append([score,titl,auth,len(sorted_mot),len(mots),ponct])

for file in glob.glob("*.*"):
  parsetexte(file)
  books.sort()

for book in books:
  print book
 
