# Import libraries

# Import files
from core import *

# Default values
default_values = {}
default_values['PASSENGER_RETURN'] = 1
default_values['PASSENGER_QUERY'] = 'select * from passengers where p_id = {0!s}'

class passenger_home(core):
	def __init__(self):
		self.cache_passenger = []
		self.bool_login = False

		self.connect_to_database()

	def check_login(self, user_id=None):
		'''
		TODO:
		PASSWORD LOGIC
		'''
		str_query = None

		try:
			if user_id is not None:
				str_query = default_values['PASSENGER_QUERY'].format(user_id)
				try:
					self.mysql_cursor.execute(str_query)
					for elem in self.mysql_cursor:
						self.cache_passenger.append(elem)

					if len(self.cache_passenger) > default_values['PASSENGER_RETURN']:
						raise Exception("Multiple user with same user ID")
					elif len(self.cache_passenger) == 0:
						raise Exception("Cannot find matching user ID")
					else:
						self.cache_passenger = self.cache_passenger[0]
						self.bool_login = True
				except Exception as e:
					print(e)
					print("Login Failed")
			else:
				raise Exception("No user ID")
		except Exception as e:
			print(e)
			print("Did not create connection to database")

	def get_login(self):
		return self.bool_login

	def reset(self):
		self.cache_passenger = []
		self.bool_login = False