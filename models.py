from sqlalchemy import Column,create_engine
from sqlalchemy import CHAR, String, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config

engine = create_engine(config.DB_CONNECT, echo=False)
Sess = sessionmaker(bind=engine)
DB = Sess()
BaseModel = declarative_base()

'''
#test
class User(BaseModel):
    __tablename__ = 'users'
    name = Column(String(10), primary_key=True)
    age = Column(Integer)
q = DB.query(User.age)
print(type(q.filter(User.name == 'oybb').all()))
print('1' == 'oybb')
'''