from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql://root:1234@localhost:3306/produtos")
Base = declarative_base()
