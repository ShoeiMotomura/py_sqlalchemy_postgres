from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

username = 'postgres'
password = 'password'
host = 'localhost'
port = '5432'
database = 'POSTGRES_SQLALCHEMY'

connection_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_url)

Session = sessionmaker(bind=engine)
session = Session()
