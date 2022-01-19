from cgitb import text
from typing import TextIO
import nltk
#Descarga un libro de inglés que ya viene tokenizado
nltk.download('book')
#Realiza la importación luego de haberlo descargado
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np
#Text1 Output = <Tex
#Se usa la función fdist para no tener que contar la cantidad de palabras que existen 
# en un texto
fdist = FreqDist(text1)
#Acá se guardan los 20 tokens más usados
#Recuerda que token son palabras y símbolos de texto
palabras_mas_usadas = fdist.most_common(20)
print(palabras_mas_usadas)
#Gráfica de plot
fdist.plot(20)
#Ver númericamente cuántas veces se repite una palabra
print(fdist['monster'])
