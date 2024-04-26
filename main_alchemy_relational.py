import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    orders = relationship("Order", back_populates="customer")

class Merchant(Base):
    __tablename__ = 'merchants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    products = relationship("Product", back_populates="merchant")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    merchant_id = Column(Integer, ForeignKey('merchants.id'))
    merchant = relationship("Merchant", back_populates="products")
    orders = relationship("OrderItem", back_populates="product")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="orders")

class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_customer(self, name, email):
        customer = Customer(name=name, email=email)
        self.session.add(customer)
        self.session.commit()
        return customer

    def get_customer_by_id(self, customer_id):
        return self.session.query(Customer).filter(Customer.id == customer_id).first()

    def update_customer_email(self, customer_id, new_email):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            customer.email = new_email
            self.session.commit()
            return True
        return False

    def delete_customer(self, customer_id):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            self.session.delete(customer)
            self.session.commit()
            return True
        return False

# Similarly, you can define methods for other CRUD operations for the remaining tables

# Example usage:
if __name__ == "__main__":
    db_url = "postgresql://username:password@localhost/dbname"
    db = Database(db_url)

    # Add a customer
    customer = db.add_customer(name="John Doe", email="john@example.com")
    print("Added Customer:", customer.id, customer.name, customer.email)

    # Update customer email
    db.update_customer_email(customer_id=1, new_email="john.doe@example.com")
    updated_customer = db.get_customer_by_id(customer_id=1)
    print("Updated Customer Email:", updated_customer.email)

    # Delete customer
    db.delete_customer(customer_id=1)
    deleted_customer = db.get_customer_by_id(customer_id=1)
    print("Deleted Customer:", deleted_customer)
