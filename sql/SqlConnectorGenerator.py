import mysql


class SqlConnectorGenerator:
    host = "localhost",
    user = "root",
    passwd = "Welcometopune18@",
    database = "DMDD"
    mydb = None

    def __init__(self, host, user, passwd, database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def createConnector(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database)
        return mydb
