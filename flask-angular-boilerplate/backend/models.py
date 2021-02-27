from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

try:
    from .config import DB_URI
except:
    from config import DB_URI

metadata = MetaData()


brand = Table('brand', metadata,
    Column('brandId', Integer, primary_key=True, autoincrement=True),
    Column('brandName', String(120), nullable=True)
)
models = Table('models', metadata,
    Column('modelsId', Integer, primary_key=True, autoincrement=True),
    Column('modelName', String(120), nullable=True)
)
fuel = Table('fuel', metadata,
    Column('fuelId', Integer, primary_key=True, autoincrement=True),
    Column('fuel', String(120), nullable=True)
)
car = Table('car', metadata,
    Column('carId', Integer, primary_key=True, autoincrement=True),
    Column('brandId', Integer, nullable=True),
    Column('modelsId', Integer, nullable=True),
    Column('year', Integer, nullable=True),
    Column('price', Integer, nullable=True),
    Column('fuelId', Integer, nullable=True),
    Column('reg', String(120), nullable=True),
    Column('color', String(120), nullable=True),
    Column('km', Integer, nullable=True)




)

# methods which should be called on the init of the database
engine = create_engine(DB_URI)
metadata.create_all(engine)
