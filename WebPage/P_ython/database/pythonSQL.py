#biblioteca de acesso ao sistema operacional
import os
import csv

#sqlalchemy é uma biblioteca para conectar o py com o sql e rodar querys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from P_ython.database import CriaDB

# database engine object from SQLAlchemy that manages connections to the database
# DATABASE_URL is an environment variable that indicates where the database lives
#engine = create_engine(os.getenv("DATABASE_URL")) 

#Como não setei nenhuma varivel de ambiente vou passar o local na mão
engine = create_engine(r'sqlite:///C:\Users\m206255\eclipse-workspace\WebPagesWithPython\WebPage\Python\database\Aeroporto.db')

# create a 'scoped session' that ensures different users' interactions with the database are kept separate
db = scoped_session(sessionmaker(bind=engine))    

def main():
    
    '''Realizando um Select'''                                                                     # 'fetchall' execute this SQL command and return all of the results
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall() 
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.") # for every flight, print out the flight info
    
    
    '''Realizando um Insert'''
    #abre um arquivo para leitura
    f = open("flights.csv")
    
    #com a biblioteca csv fazemos a leitura do arquivo aberto
    reader = csv.reader(f)
     
    # loop gives each column a name
    for origin, destination, duration in reader:
        # os valores marcados como ":" seram marcados como ponto para serem substituidos pela proxima linha de parametros
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                  {"origin": origin, "destination": destination, "duration": duration}) 
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    
    # transactions are assumed, so close the transaction finished     
    db.commit()
        
if __name__ == "__main__":    
    #cria o banco de dados SQLite3
    CriaDB.__init__()
    main()
        