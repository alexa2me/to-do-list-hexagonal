from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base


# Define a classe Base personalizada
class CustomBase:
    metadata = MetaData()


# Cria uma instância de declarative_base com a classe Base personalizada
Base = declarative_base(cls=CustomBase)
