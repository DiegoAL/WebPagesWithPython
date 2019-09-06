from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

#Para cada tabela no banco de dados sera necessario criar uma classe
#O uso do 'db.Model'defini um processo de herança
#O 'db.Column' cria um novo campo na tabela
class Flight(db.Model):
    #Este parametro defini o nome da tabela no banco de dados
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    #Passengers não é uma coluna da tabela Flight
    #Isso é apenas algo que existe no lado python para definir o relacionamento de tabelas
    #Com isso torna-se mais facil extrair os passageiros de um voo, não sendo necessario realizar uma query com join
    #O "lazy=True" é uma propriedade que indica a classe que somente quando algo invocar esse relecionarmento ele deverá ser processado
    #    ou seja, a classe não fica perdendo tempo tentando realizar o relacionamento
    #com isso para buscar todos os passageiros de um voo basta dizer:
    #    passegeiro = flight.passengers
    # ao inves de:
    #     passageiro = Passenger.query.filter_by(flight_id = flight_id).all
    passengers = db.relationship("Passenger", backref="flights", lazy=True)
    
    #com esse metodo tornamos mais facil adicionar novos passageiros no voo, sendo apenas necessario chamar o metodo
    def add_Passenger(self, name):
        passenger = Passenger(name = name,flight_id = self.id )
        db.session.add(passenger)
        db.session.commit()


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    #a propriedade 'db.ForeignKey' defini um relacionamento de chave estrangeira, 
        #sendo que o valor (flights.id) corresponde ao nome da tabela e não da classe
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)