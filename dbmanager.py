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
    			 
            #self.conn = pypyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'LAPTOP-HG7BB9JM' , database = 'WareHubDB')	 
			self.cursor = conn.cursor()
		except:
			pass
	


	def executeQuery(self, query):
		self.data = self.cursor.execute(query)
		self.data = self.data.fetchall()
		return self.data

	def executeNonQuery(self, query):
		self.cursor.execute(query)
		self.conn.commit()


	def closeConnection(self):
		self.conn.close()

