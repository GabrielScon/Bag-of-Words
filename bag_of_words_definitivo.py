
#Aluno: Gabriel Sposito Conciani.

#Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e 
#imprimir esta matriz na tela. Para tanto: 
#a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores, 
#onde cada item será uma das palavras da sentença. 
#b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores, 
#onde cada item será um lexema.  
#c) Este único corpus será usado para gerar o vocabulário. 
#d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da 
#técnica bag of Words em todo o corpus.  

from bs4 import BeautifulSoup
import requests
import spacy

spa = spacy.load("en_core_web_sm")

url1 = "https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1"
url2 = "https://www.ibm.com/cloud/learn/natural-language-processing"
url3 = "https://en.wikipedia.org/wiki/Natural_language_processing"
url4 = "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP"
url5 = "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/"

html1 = requests.get(url1)
html2 = requests.get(url2)
html3 = requests.get(url3)
html4 = requests.get(url4)
html5 = requests.get(url5)

sp1 = BeautifulSoup(html1.text,"html.parser").find("p").get_text()
sp2 = BeautifulSoup(html2.text,"html.parser").find("p").get_text()
sp3 = BeautifulSoup(html3.text,"html.parser").find("p").get_text()
sp4 = BeautifulSoup(html4.text,"html.parser").find("p").get_text()
sp5 = BeautifulSoup(html5.text,"html.parser").find("p").get_text()

stopwords=["to","is","a"]
pontuaçao=[",",":"," ",";",".","?","(",")"]

def sentensas_palavras(sentensas):
  palavras = spa(sentensas)
  return [palavras.orth_ for palavras in palavras]

sentensas1 = sentensas_palavras(sp1)
sentensas2 = sentensas_palavras(sp2)
sentensas3 = sentensas_palavras(sp3)
sentensas4 = sentensas_palavras(sp4)
sentensas5 = sentensas_palavras(sp5)


def vetorizar(sentensas):
    vetor=[]
    for v in vocabulario:
        vetor.append(sentensas.count(v))
    return vetor

def unir(sequence):
    b = set()
    return [a for a in sequence if not (a in b or b.add(a))]

vcb = unir(sentensas1 + sentensas2 + sentensas3 + sentensas4 + sentensas5)
vocabulario=[]

for s in vcb: 
    if s not in stopwords and s not in pontuaçao: 
       vocabulario.append(s)

vetor1=vetorizar(sentensas1)
vetor2=vetorizar(sentensas2) 
vetor3=vetorizar(sentensas3) 
vetor4=vetorizar(sentensas4) 
vetor5=vetorizar(sentensas5)

print("-----------------------------------------------------------------------")
print(sentensas1)
print(sentensas2)
print(sentensas3)
print(sentensas4)
print(sentensas5)
print("-----------------------------------------------------------------------")

print("Palavras: ",vocabulario)
print("Site 1: ",vetor1)
print("Site 2: ",vetor2) 
print("Site 3: ",vetor3) 
print("Site 4: ",vetor4) 
print("Site 5: ",vetor5)
