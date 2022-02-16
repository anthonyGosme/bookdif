from __future__ import division
import operator
import re
import unidecode
import glob
import math

books =[]

def parsetexte(file):
  print(file)
  f = open(file, "r")
  texte = f.read(1111).lower()
  title = re.search(r'title: (.*)', texte)
  author = re.search(r'author: (.*)', texte)
  language = re.search(r'language: (.*)', texte)
  if not title :
    print("no title"  + file)
    return
  if not author :
    auth = "none"
  else :
    auth = re.sub('[^a-zA-Z]+', ' ', author.group(1))
  if not language :
    language = "none"
  else :
    language = re.sub('[^a-zA-Z]+', ' ', language.group(1))



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
  uniqueWord = sorted(tf.items(), key=operator.itemgetter(1))
  score = int(10*len(uniqueWord)/(math.sqrt(len(mots))+math.sqrt(ponct*5)))
  books.append([score,titl,auth,len(uniqueWord),len(mots),ponct,language])

for file in glob.glob("./txt/*.*"):
  print("l")
  parsetexte(file)
  books.sort()
 
html =  """
<!doctype html>
<html lang="en">
<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
<table class="table">
  <thead>
    <tr>
      <th scope="col">Score</th>
      <th scope="col">Book</th>
      <th scope="col">Author</th>
      <th scope="col">unique words</th>
      <th scope="col">total words</th>
      <th scope="col">total lines</th>
      <th scope="col">language</th>
    </tr>
"""

for book in books:
  print book
  html = html +"<tr><td>" +str(book[0])\
  +"</td><td>"+str(book[1])\
  +"</td><td>"+str(book[2])\
  +"</td><td>"+str(book[3])\
  +"</td><td>"+str(book[4])\
  +"</td><td>"+str(book[5])\
  +"</td><td>"+str(book[6])
 
html = html +  "</tbody></table></body></html>"
f = open("resut.html", "w")
f.write(html)
f.close()
print (html)