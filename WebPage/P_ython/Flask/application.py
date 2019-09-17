'''
Created on 26 de jul de 2019

@author: Diego Alves A. (diego.assis@enel.com)

'''
from flask import Flask, render_template, request, session, jsonify
from flask_session import Session

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


#Enviando informações entre paginas com formularios
#Dentro do 'methods' é descrito todos os metodos que serõa aceitos pelo codigo,
    #outros metodos serão ignorados, gerando um erro para o usuario.
@app.route('/formularios', methods=["POST", "GET"])
def workingForulario():
    if request.method == "GET":
        return "Favor submeter esta pagina via POST"
    else:
        #A biblioteca 'request' é responsavel por pegar informações de formularios
        nome = request.form.get('nome')
        return render_template("recebendoFormulario.html", nome=nome)
    

#Armazenando informações em uma sessão no lado do servidor
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#utilizar um variavel 'global' ou seja declarada fora de um metodo permite que varios usuarios a utilizem e atualizem a aplicacao
#entretanto sem utilizar uma sessao esses dados são apagados quando o servidor é reiniciado
#o pacote 'session' do Flask permite criar sessoes individuais
#já o pacote 'Session" do flask_session tem features adicionais para maior controle como por exemplo armazenar as informações no server-side

@app.route('/sessao', methods=['POST', 'GET'])
def sessao():
    #com o session[] é definido que a lista pertence a uma sessao unica
    if session.get('notes') is None:
        session['notes'] = []
    if request.method == 'POST':
        session['notes'].append(request.form.get('nota'))
    
    return render_template('Pagina.html', notes = session['notes'])


#Para criarmos uma API basta utilizar um metodo de comunicação que seja padronizado, neste caso JSON
@app.route('/API/<int:myid>')
def myApi(myid):
    if myid == 1:
        return jsonify({"error" : "O ID informado é invalido!"}), 422
    else:
        return jsonify({"var1" : "valor do parametro 1",
                        "var2" : "ola",
                        "var3" : "e assim por diante..."})
    