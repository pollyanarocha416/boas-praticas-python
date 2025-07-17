from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# mydb = mysql.connector.connect(host="localhost", user="root", password="1234")

# print(mydb)

# Definindo a engine do banco de dados
engine = create_engine("mysql://root:1234@localhost:3306/produtos")
Base = declarative_base()
