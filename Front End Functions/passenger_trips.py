# Import libraries

# Import files
from passenger_home import *

# Default values
default_values = {}

class passenger_trips(passenger_home):
	def __init__(self, cache_passenger):
		self.purchase_time=None
		self.destination=None
		self.date=None

		try:
			self.purchase_time = cache_passenger['purchaseTime']
			self.destination = cache_passenger['destination']
			self.date=cache_passenger['date_']
		except Exception as e:
			print(e)

	def get_purchase_time(self):
		return str(self.purchase_time)

	def get_purchase_date(self):
		return str(self.date)

	def get_destination(self):
		return str(self.destination)