from sqlalchemy import Column, Integer, String, ForeignKey
from passlib.hash import sha256_crypt
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    username = Column(String(255), unique=False, nullable=False)
    password = Column(String(255), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)

    def hash_password(self, password):
        self.password = sha256_crypt.encrypt(password)


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine("postgresql://homestead:secret@localhost/backend")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
