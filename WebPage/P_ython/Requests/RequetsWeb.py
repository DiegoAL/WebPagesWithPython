'''
Created on 11 de set de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
import requests

#Realizando uma requisição get sem parametros
req = requests.get('https://www.google.com.br', params={"parametro1" : "valor", "parametro2" : "valor2"})

if req.status_code != 200:
    #raise é uma forma de forçar o encerramento da execução do programa
    raise Exception("Erro durante processamento do programa")

###!!!A pagina do google n retorna um json, esse trecho é apenas um exemplo.!!!
retornoJson = req.json()

print(retornoJson)
