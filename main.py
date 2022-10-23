from pywinauto import Application # pip install pywinauto
from bs4 import BeautifulSoup
import requests
import azure.functions

#Pregunta por el perfil del usuario (puede seleccionar más de uno)
mujer=int(input("mujer "))
lgbt=int(input("lgbt "))
ind=int(input("ind "))
afr=int(input("afr "))
mig=int(input("mig "))
#Lista todas las palabras de acuerdo al perfil
wordsList2=[]
wordsList=[]
if mujer==1:
    with open('women_words.txt','r',encoding='utf-8') as file:
        for line in file:
            wordsList.append(line)
if lgbt==1:
    with open('lgbt_word.txt','r',encoding='utf-8') as file:
        for line in file:
            wordsList.append(line) 
if ind==1: 
    with open('ind_words.txt','r',encoding='utf-8') as file:
        for line in file:
            wordsList.append(line)   
if afr==1: 
    with open('afr_words.txt','r',encoding='utf-8') as file:
        for line in file:
            wordsList.append(line)  
if mig==1: 
    with open('mig_words.txt','r',encoding='utf-8') as file:
        for line in file:
            wordsList.append(line)    
for word in wordsList:
    word=word.replace("\n","")
    wordsList2.append(word)  

print(wordsList2)
wordsList.clear()
#Request momentaneo para las páginas web
app = Application(backend='uia')
app.connect(title_re=".*Chrome.*")
element_name="Address and search bar"
dlg = app.top_window()
url = dlg.child_window(title=element_name, control_type="Edit").get_value()
url="http://"+url
print(url)
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
soup=str(soup).lower()
#Búsqueda de palabras. Al detectar una, notifica al usuario.
for word in wordsList2:
    if  soup.find(word)!=-1:
        print("Existe palabra ofensiva: " + word)
        break


