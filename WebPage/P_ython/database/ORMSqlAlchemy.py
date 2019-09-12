#import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from sqlalchemy import and_

#classe para ser utilizada no processo de consulta ao banco de dados
from .ModelTable import Flight, Passenger

app = Flask(__name__)

# Tell Flask what SQLAlchemy database to use.
#Acessando via variavel de ambiente
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = r'sqlite:///Aeroporto.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
#db = SQLAlchemy()
#db.init_app(app)
db = SQLAlchemy(app)

def main():
        
    # Create tables based on each table definition in `models`
    db.create_all()
    
    
    #Realizando INSERT
    #Unitario
    flight1 =  Flight (origin = 'Brazil', destination = 'New york', duration = '2840')
    db.session.add(flight1)
    
    #Atraves de uma lista
    flightsList = [Flight(origin = 'New York', destination = 'Brazil', duration = '742'),
                   Flight(origin = 'Germany', destination = 'Brazil', duration = '1241'),
                   Flight(origin = 'New York', destination = 'Germany', duration = '7200'),
                   Flight(origin = 'Brazil', destination = 'Canada', duration = '810'),
                   Flight(origin = 'Canada', destination = 'China', duration = '3840')]
    db.session.add_all(flightsList)
    
    #para gravar é necessario realizar o commit
    db.session.commit()
    
    
    #Realizando SELECTS
    
    #Selecionando todos os registros 'SELECT * FROM' e retorna uma lista
    flights = Flight.query.all() 
    #imprime cada registro do banco encontrado pela query
    for ft in flights:
        print(f'Origem: {ft.origin} | Destino: {ft.destination} | Tempo: {ft.duration} minutos')
    
    #Utilizando paramentros como um 'WHERE'
    
    #O 'all()' neste caso retorna todos os registros encontrados
    Flight.query.filter_by(origin = 'New york').all()
    
    #O 'first' retorna apenas a primeira linha
    Flight.query.filter_by(origin = 'New york').first()
    
    #realizando um count
    Flight.query.filter_by(origin = 'New york').count()
    
    #realizando a busca por ID (Primary Key)
    Flight.query.filter_by(id = 2).first()
    #Entretanto existe uma função mais eficiente para seleção de PK
    Flight.query.get(2)
    
    #Ordenação 'ORDER BY'
    Flight.query.order_by(Flight.origin).all()
    
    ##Ordenação 'ORDER BY' informando se DESC ou ASC
    Flight.query.order_by(Flight.origin.desc()).all()
    
    #Realizando filtro com parametros booleanos, por exemplo 'não igual'
    Flight.query.filter(Flight.origin != 'New york').all()
    
    #Procurando por um valor aproximado 'LIKE'
    Flight.query.filter(Flight.origin.like('%o%')).all
    
    #Procurando por valores que estejam em um range 'IN'
    #é necessario utilizar o "_" para diferenciar o in da biblioteca python do in do sqlalchemy
    Flight.query.filter(Flight.origin.in_(['Brazil', 'New York'])).all
    
    #realizando querys com "AND" e "OR"
    Flight.query.filter(and_(Flight.origin == 'Paris', Flight.duration > 500)).all
    Flight.query.filter(or_(Flight.origin == 'Paris', Flight.duration > 500)).all
    
    #realizando select com "JOIN" para relacionamento entre tabelas
    db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
    
    #Selecionando todos os voos de um passageiro atraves de relacionamento
    #SELECT * FROM passengers WHERE flight_id = 1
    Flight.query.get(1).passengers
    
    #Selecionando todos os voos onde um determinado passageiro esta
    #SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE passengers.name = 'Diego';
    #Passenger.query.filter_by(name = 'Diego').first().flight
    
    
    #Realizando UPDATE
    #Primmeiramente é necessario obter o objeto do banco
    fupdate = Flight.query.get(1)
    #O update ocorre quando o valor de um campo é alterado
    fupdate.duration = 300
    
    
    #Realizando DELETE
    #Primmeiramente é necessario obter o objeto do banco
    fdelete = Flight.query.get(3)
    #db.session.delete(fdelete)
    
    #efetiva a deleção no banco
    db.session.commit()

    
@app.route('/')
def index():
    main()
    return 'Executado'    

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()