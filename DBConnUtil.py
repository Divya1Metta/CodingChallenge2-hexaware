from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def getDBConn():
  
        """
        Establish a connection to the database and return the database Connection
        """
        conn_str = ("Driver={Devart ODBC Driver for SQL Server};"
                    "Server=myserver;Database=mydatabase;Port=myport;"
                    "User ID=myuserid;Password=mypassword")
        try:
            cnxn = pyodbc.connect(conn_str)
            return cnxn
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            return None