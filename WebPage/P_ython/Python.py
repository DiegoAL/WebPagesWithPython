'''
Created on 15 de jul de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''

name = input("digite seu nome: ")
#Passando variaveis dentro de uma string
#f -> for match strings
print(f"Ola, {name}!")

#deixar a primeira letra em maiusculo
name = "diego"
name = name.capitalize()


#metodo
def newMethod(x):
    return x * x

def main():
    for x in range(10):
        print(newMethod(x))

#essa validação server para que caso este codigo seja consulmido como uma biblioteca somente o methodo invocado seja utilizado
    #caso contrario todos código seria executado, por isso o methodo main e o if abaixo
    #ou seja toda a logica deste programa somente é executada se este programa for executado
if __name__ == "__main__":
    main()
    