# Import libraries

# Import files
from passenger_home import *

# Default values
default_values = {}

class passenger_checkin(passenger_home):
	def __init__(self, cache_passenger):
		self.passenger_id=None
		self.last_name=None
		self.first_name=None

		try:
			self.passenger_id = cache_passenger['P_id']
			self.last_name = cache_passenger['Lname']
			self.first_name = cache_passenger['Fname']
		except Exception as e:
			print(e)

	def get_ticket_number(self):
		return str(self.passenger_id)

	def get_passenger_name(self):
		return str("{0!s} {1!s}".format(self.first_name, self.last_name))