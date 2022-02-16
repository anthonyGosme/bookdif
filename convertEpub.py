
import ebooklib
import re
from ebooklib import epub


book = epub.read_epub('./epub/Camus-L_Etranger.epub')
#for image in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
texte =""
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
       texte = texte + item.get_content()

print(book.get_metadata('DC', 'author'))   

title = book.get_metadata('DC', 'title')
#texte =  
print ((title[0][0]))
f = open("./txt/"+title[0][0]+".txt", "w")
f.write("title: "+ title[0][0].encode('utf-8')+"\n")
f.write(texte)
f.close()