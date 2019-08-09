'''
Created on 26 de jul de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
from flask import Flask, render_template
import datetime

#para rodar uma aplicação feita em flask é necessario acessar o terminal e digitar:
#    flask run
#No output do programa estara onde a web app está rodando

#Esta linha defini uma nova web application Flask, o __name__ diz que este arquivo representar a app
app = Flask(__name__)

#O flask é desenhado por rotas
#/ representar a pagina principal

#Quando o usuario for para a pagina principal o metodo abaixo a anotação será executado
@app.route("/")
def index():
    return "Hello Flask"


#criando uma outra pagina
@app.route("/diego")
def pgDiego():
    return "Oi Diego"


#identificando qualquer rota que o usuario digitar e interagindo com o nome desta rota
@app.route("/<string:name>")
def pgQualquerNome(name):
    #deixando a primeira letra em maiusculo
    name = name.capitalize()
    #é possivel retornar codigo html diretamente pelo python, mas não é viavel fazer isso
    return f"<h1>Ola, {name}</h1>"


#para referenciar a paginas html e necessario utilizar uma funcao especifica do flask chamada "render_template"
#é obrigatorio que a pagina esteja na pasta "templates"
@app.route("/usinghtml")
def usingHtml():
    pythonVariable = 'valor inserido via python'
    return render_template("Pagina.html", pythonVariable = pythonVariable)

#e possivel numa mesma pagina html alterar o valor da variavel sem que isso influencie outros codigos
#    neste exemplo para a mesma pagina html, a rota é diferente mas a variavel que tem o valor alterado é a mesma
#    que a rota acima
@app.route("/usinghtml2")
def mesmoHtml():
    pythonVariable = 'um outro valor enviado via python'
    return render_template("Pagina.html", pythonVariable = pythonVariable)


#apartir do valor passado no pagametro o python embarcado no html ira decidir (pelo if) qual condigo renderizar 
@app.route("/condicoes")
def condicoes():
    now = datetime.datetime.now()
    anoNovo = now.month == 1 and now.day == 1
    return render_template("Pagina.html", anoNovo = anoNovo)


#passando uma lista e exibindo cada valor dentro de um loop (for)
@app.route("/loop")
def htmlLoop():
    nameList = ['Diego', 'Franciele', 'Miguel', 'Helena']
    return render_template("Pagina.html", names = nameList)


#trabalhando com link de paginas (uma apontando para outra)
@app.route('/paginaLinkada1')
def paginaLink1():
    return render_template("Pagina.html")

@app.route('/paginalinkada2')
def paginaLink2():
    return render_template('PaginaLinkada.html')


#utilizando uma pagina como layout e outras herdando ela e modificando o conteudo
@app.route('/utilizandoLayout')
def useLayout():
    return render_template('usandoLayout1.html')

@app.route('/utilizandoLayout2')
def useLayout2():
    return render_template('usandoLayout2.html')