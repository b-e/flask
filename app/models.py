from app import db
from sqlalchemy import Column, Integer, String
'''
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Registry(Base):
	'''
class Registry(db.Model)
	__tablename__ = 'registry'

	id = Column(Integer, primary_key=True)
	token = Column(String)
	endpoint = Column(String)
	phoneNumber = Column(Integer)
	channel = Column(String)
	pid = Column(Integer)

	def __repr__(self):
		return 'phoneNumber {}'.format(self.phoneNumber)