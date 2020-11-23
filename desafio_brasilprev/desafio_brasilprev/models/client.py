from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float

from sqlalchemy.orm import relationship

from ..models import Base


association_table = Table(
    'client_product', Base.metadata,
    Column('client_id', Integer, ForeignKey('client.id')),
    Column('product_id', Integer, ForeignKey('product.id'))
)


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    
    products = relationship('Product', secondary=association_table)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    code = Column(Integer, nullable=False, unique=True)
    price = Column(Float, nullable=False)
