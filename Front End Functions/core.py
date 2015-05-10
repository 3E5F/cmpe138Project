# Library imports
import mysql.connector

# Default Values
default_values = {}
default_values['USERNAME'] = 'user'
default_values['PASSWORD'] = 'p4sswurd'
default_values['HOST'] = '67.169.34.164'
default_values['DATABASE'] = 'train_project'

class core(object):
	def __init__(self):
		self.mysql_connector = None
		self.mysql_cursor = None

	def connect_to_database(self, db_user=default_values['USERNAME'], db_password=default_values['PASSWORD'], db_host=default_values['HOST'], db_database=default_values['DATABASE']):
		try:
			self.mysql_connector = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_database)
			self.mysql_cursor = self.mysql_connector.cursor(dictionary=True)
		except Exception as e:
			print(e)