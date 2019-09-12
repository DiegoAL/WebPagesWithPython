'''
Created on 11 de set de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
import requests

#Realizando uma requisição get sem parametros
req = requests.get('http://www.google.com.br')
print(req.text)
