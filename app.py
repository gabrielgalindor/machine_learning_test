from cgitb import text
from typing import TextIO
import nltk
#Descarga un libro de inglés que ya viene tokenizado
nltk.download('book')
#Realiza la importación luego de haberlo descargado
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np
#Text1 Output = <Text: Moby Dick by Herman Melville 1851>
#Obtenemos tokenizado las primeras palabras partiendo de la descarga de ntlk
text1.tokens[:20]
print(text1)
#Para obtener los valores de la formula de la fig. 1. 
# Podemos utilizar la función set
#vocabulario = set(text1)
#print(vocabulario)
#La función set retorna un diccionario
#por lo que para convertirlo en lista y poder usar la fun len()
def get_riqueza_lexica(texto):
    vocabulario = sorted(set(texto))
    long_vocabulario = len(vocabulario)
    long_texto = len(texto)
    riqueza_lexica = long_vocabulario/long_texto
    return riqueza_lexica

#Otra variable importante es porcentaje de palabra
def porcentaje_palabra(palabra, texto):
    return 100*texto.count(palabra)/len(texto)

#Se obtiene la riqueza léxica del text1
rlexica_txt1 = get_riqueza_lexica(text1)
print(rlexica_txt1)
#Se calcula el porcentaje de la palabra monster
monster_porcent = porcentaje_palabra('monster', text1)
print(monster_porcent)