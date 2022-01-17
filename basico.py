import nltk
import re
#Descarga el Coroues
nltk.download('cess_esp')
corpus = nltk.corpus.cess_esp.sents()
#print(corpus)
#print(len(corpus))
#Obtiene cada palabra tokenizada del corpus
flatten = [w for l in corpus for w in l ]
#print(len(flatten))
#Realiza la busqueda según la expresión regular
lista = [w for w in flatten if re.search('.s', w)]
#print(lista)

#Patrón especial para tokenizar de manera sencilla teniendo en cuenta variaciones del idioma como signos, entre otros, etc. 
pattern = r'''(?x)                  # Flag para iniciar el modo verbose
              (?:[A-Z]\.)+            # Hace match con abreviaciones como U.S.A.
              | \w+(?:-\w+)*         # Hace match con palabras que pueden tener un guión interno
              | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
              | \.\.\.              # Hace match con puntos suspensivos
              | [][.,;"'?():-_`]    # Hace match con signos de puntuación
'''

texto = "Mucha mierda nos está jodiendo la cabeza. En U.S.A. me pongo a pensar ¿Será qué soy un puto?"
print(nltk.regexp_tokenize(texto, pattern))