from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('mysql+mysqlconnector://your_username:your_password@localhost/your_database')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    balance = Column(Integer)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Integer)
    account = relationship(Account, backref='transactions')


@event.listens_for(Transaction, 'before_insert')
def update_balance(mapper, connection, target):
    connection.execute(Account.__table__.update().where(Account.id == target.account_id).values(balance=Account.balance + target.amount))


def insert_transaction(account_id, amount):
    transaction = Transaction(account_id=account_id, amount=amount)
    session.add(transaction)
    session.commit()
    print("Transaction inserted successfully.")

Base.metadata.create_all(engine)

insert_transaction(1, 100)
