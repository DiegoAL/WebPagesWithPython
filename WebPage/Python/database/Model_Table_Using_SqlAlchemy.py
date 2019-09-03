from flask_sqlalchemy import SQLAlchemy

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


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    #a propriedade 'db.ForeignKey' defini um relacionamento de chave estrangeira, 
        #sendo que o valor (flights.id) corresponde ao nome da tabela e não da classe
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)