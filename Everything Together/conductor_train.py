# Import libraries

# Import files
from conductor_home import *

# Default values
default_values = {}
default_values['CONDUCTOR_QUERY'] = 'select * from controlled_by where B_id = {0!s}'
default_values['TRAIN_RETURN'] = 1

class conductor_trains(core):
	def __init__(self, cache_conductor):
		self.conductor_id=None
		self.cache_train = []
		try:
			self.conductor_id = str(cache_conductor['C_id'])
		except Exception as e:
			print(e)

		self.connect_to_database()

	def query_conductor_information(self):
		query = None

		try:
			if self.conductor_id is not None:
				query = default_values['CONDUCTOR_QUERY'].format(self.conductor_id)
				self.mysql_cursor.execute(query)
				for elem in self.mysql_cursor:
					self.cache_train.append(elem)

					if len(self.cache_train) > default_values['TRAIN_RETURN']:
						raise Exception("Mulitple trains with the same conductor ID")
					else:
						self.cache_train = self.cache_train[0]
			else:
				raise Exception("No conductor ID")
		except Exception as e:
			print(e)
			print("Did not retrieve conductor train information")

	def get_conductor_id(self):
		return str(self.conductor_id)

	def get_conductor_train(self):
		return str(self.cache_train['ctrain_no'])