# Import libraries

# Import files
from core import *

# Default values
default_values = {}
default_values['TRAIN_RETURN'] = 5
default_values['TRAIN_QUERY'] = 'select * from train'

class train_schedules(core):
	def __init__(self):
		self.cache_train = []
		self.return_dictionary = {}

		self.connect_to_database()

	def query_train_schedules(self):
		str_query = None
		
		try:
			str_query = default_values['TRAIN_QUERY']
			self.mysql_cursor.execute(str_query)

			for elem in self.mysql_cursor:
				self.cache_train.append(elem)

			if len(self.cache_train) > default_values['TRAIN_RETURN']:
				raise Exception("Error in reading train query")
			else:
				for elem in self.cache_train:
					self.return_dictionary[str(elem['train_no'])] = {'seat_cap':str(elem['max_cap']), 'cabin_temp':str(elem['cabin_temp']), 'status':str(elem['status_']), 'recent_location':str(elem['last_known_loc'])}
		except Exception as e:
			print(e)

	def get_seat_cap(self, train):
		return str(self.return_dictionary[str(train)]['seat_cap'])

	def get_recent_location(self, train):
		return str(self.return_dictionary[str(train)]['recent_location'])

	def get_cabin_temp(self, train):
		return str(self.return_dictionary[str(train)]['cabin_temp'])

	def get_status(self, train):
		return str(self.return_dictionary[str(train)]['status'])

	def get_train_information(self, train):
		return dict(self.return_dictionary[str(train)])