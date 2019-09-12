'''
Created on 9 de set de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
import sqlite3

def __init__():
    print('Banco de dados criado')
    conn = sqlite3.connect('Aeroporto.db')
    conn.close()
    
if __name__ == '__main__':
    __init__()