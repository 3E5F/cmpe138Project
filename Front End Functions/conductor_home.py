# Import libraries

# Import files
from core import *

# Default values
default_values = {}
default_values['CONDUCTOR_RETURN'] = 1

class conductor_home(core):
	def __init__(self):
		self.cache_conductor = []
		self.bool_login = False

		self.connect_to_database()

	def check_login(self, conductor_id=None):
		'''
		TODO:
		PASSWORD LOGIC
		'''
		str_query = None

		try:
			if conductor_id is not None:
				str_query = 'select * from conductor where C_id = {0!s}'.format(conductor_id)
				try:
					self.mysql_cursor.execute(str_query)
					for elem in self.mysql_cursor:
						self.cache_conductor.append(elem)

					if len(self.cache_conductor) > default_values['CONDUCTOR_RETURN']:
						raise Exception("Multiple conductor with same conductor ID")
					elif len(self.cache_conductor) == 0:
						raise Exception("Cannot find matching conductor ID")
					else:
						self.cache_conductor = self.cache_conductor[0]
						self.bool_login = True
				except Exception as e:
					print(e)
					print("Login Failed")
			else:
				raise Exception("No conductor ID")
		except Exception as e:
			print(e)
			print("Did not create connection to database")