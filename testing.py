from cgitb import text
from typing import TextIO
import nltk
import matplotlib.pyplot as plt
import numpy as np
from nltk.book import *

pattern = r'''(?x)                  # Flag para iniciar el modo verbose
              (?:[A-Z]\.)+            # Hace match con abreviaciones como U.S.A.
              | \w+(?:-\w+)*         # Hace match con palabras que pueden tener un guión interno
              | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
              | \.\.\.              # Hace match con puntos suspensivos
              | [][.,;"'?():-_`]    # Hace match con signos de puntuación
'''

text_file = open("testing1.txt", "r")
data = text_file.read()
text_file.close()
texto_tokenizado = nltk.regexp_tokenize(data, pattern)
fdist_texto = FreqDist(texto_tokenizado)
palabras_mas_usadas = fdist_texto.most_common(20)
print(palabras_mas_usadas)