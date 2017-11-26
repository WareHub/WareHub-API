import pypyodbc

class DBManager:
	def __init__(self):
		try:
			self.conn = pypyodbc.connect(
    			 r'DRIVER={ODBC Driver 11 for SQL Server};'
   				 r'SERVER=omarsgalal.database.windows.net;'
   				 r'DATABASE=WareHubDB;'
   				 r'UID=omarsgalal;'
   				 r'PWD=123456Omar'
    			 )
			self.cursor = conn.cursor()
		except:
			pass


	def executeCommand(self, query):
		self.data = cursor.execute(query)
		self.conn.commit()


	def closeConnection(self):
		self.conn.close()