from sqlalchemy import Column, Integer, String, ForeignKey
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    username = Column(String(140), unique=False, nullable=False)
    password = Column(String(140), nullable=False)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from db_config import DB_URI

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
