from sqlalchemy import Column, Integer, String
from app.database import Base

class Registry(Base):
	__tablename__ = 'registry'

	id = Column(Integer, primary_key=True)
	token = Column(String)
	endpoint = Column(String)
	phoneNumber = Column(Integer)
	channel = Column(String)
	pid = Column(Integer)

	def __init__(self, token=None, endpoint=None, phoneNumber=None, channel=None, pid=None):
		self.token = token
		self.endpoint = endpoint
		self.phoneNumber = phoneNumber
		self.channel = channel
		self.pid = pid

	def __repr__(self):
		return 'phoneNumber {}'.format(self.phoneNumber)