import ebooklib


from ebooklib import epub
book = epub.read_epub('./epub/Camus-L_Etranger.epub')
#for image in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
texte =""

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
       texte = texte + item.get_content()

author = book.get_metadata('DC', 'creator')[0][0]

title = book.get_metadata('DC', 'title')[0][0]
language= book.get_metadata('DC', 'language')[0][0]
#texte =  


f = open("./txt/"+title+".txt", "w")
f.write("title: "+ title.encode('utf-8')+"\n" +"author: "+author +"\nlanguage: "+language +"\n")
f.write(texte)
f.close()