# Import libraries

# Import files
from conductor_home import *

# Default values
default_values = {}
default_values['QUERY_UPDATE_STATUS'] = "update train set status_='{0!s}' where train_no='{1!s}'"

class update_status(core):
	def __init__(self):
		self.connect_to_database()

	def update_train_status(self, train_number=None, status=None):
		query = None
		try:
			query = default_values['QUERY_UPDATE_STATUS'].format(str(status), str(train_number))
			self.mysql_cursor.execute(query)
			self.mysql_connector.commit()
		except Exception as e:
			print(e)