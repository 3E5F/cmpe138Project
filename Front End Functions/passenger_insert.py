# Import libaries
import random
import time

# Import files
from core import *

# Default vales
default_values = {}
default_values['PASSENGER_LOW'] = 0
default_values['PASSENGER_HIGH'] = 999999999
default_values['QUERY_CHECK_PASSENGER'] = "select P_id from passengers"
default_values['QUERY_UPDATE_BUY'] = "insert into buy values ('{0!s}', '{1!s}')"
default_values['QUERY_UPDATE_RIDE'] = "insert into ride values ('{0!s}', '{1!s}')"
default_values['QUERY_UPDATE_TICKETS'] = "insert into tickets values ('{0!s}', '{1!s}, '{2!s}', '{3!s}')"
default_values['QUERY_INSERT_PASSENGER'] = "insert into passengers values ('{0!s}', '{1!s}', '{2!s}', '{3!s}', '{4!s}', '{5!s}')"
default_values['QUERY_VERIFIES_TICKET'] = "insert into verifies_ticket values ('{0!s}', '{1!s}')"

#426432706


class passenger_insert(core):
	def __init__(self):
		random.seed()
		self.connect_to_database()

	def insert_user(self,first_name=None, last_name=None, destination=None):
		self.passenger_id = None
		self.current_time = None
		self.current_date = None
		query = []
		current_passenger_id = []

		try:
			self.mysql_cursor.execute(default_values['QUERY_CHECK_PASSENGER'])

			for elem in self.mysql_cursor:
				current_passenger_id.append(str(elem['P_id']))

			self.first_name = first_name
			self.last_name = last_name
			self.destination = destination
			self.passenger_id = str(int(random.triangular(default_values['PASSENGER_LOW'], default_values['PASSENGER_HIGH'])))
			self.current_time = str(time.strftime("%H:%M:%S"))
			self.current_date = str(time.strftime("%Y-%m-%d"))

			while self.passenger_id in current_passenger_id:
				self.passenger_id = str(int(random.triangular(default_values['PASSENGER_LOW'], default_values['PASSENGER_HIGH'])))

			query.append(default_values['QUERY_INSERT_PASSENGER'].format(self.passenger_id, self.first_name, self.last_name, self.current_date, self.current_time, self.destination))
			query.append(default_values['QUERY_UPDATE_BUY'].format(self.current_time, self.destination))

			# TODO: UPDATE RIDE WITH CORRECT TRAIN
			# query.append(default_values['QUERY_UPDATE_RIDE'].format(self.train_no, self.passenger_id))
			# TODO: UPDATE RIDE WITH CORRECT TRAIN AND TICKET
			# query.append(default_values['QUERY_UPDATE_TICKETS'].format(self.destination, self.passenger_id, self.train_no, self.passenger_id))
			# TODO: UPDATE VERIFIES_TICKET WITH CORRECT CONDUCTOR BASED ON TRAIN
			# query.append(default_values['QUERY_VERIFIES_TICKET'].format(None, self.passenger_id))
			for elem in query:
				self.mysql_cursor.execute(elem)
		
			self.mysql_connector.commit()
		except Exception as e:
			print(e)

	def get_passenger_id(self):
		return str(self.passenger_id)