import sqlite3
from priceData import PriceData


# Create fake data
fakeData = PriceData("2020-10-23 22:12:11.123", 10000.142)

class DataBaseManager:
    """
        This class creates and manages the priceData dabase
    """
    def createDataBase(self, dataBaseName):
        self.conn = sqlite3.connect(dataBaseName + ".db")
    
    def connectToDataBase(self, dataBaseNameToConnectTo):
        self.conn = sqlite3.connect(dataBaseNameToConnectTo)
        self.c = self.conn.cursor()

    def createTableInDataBase(self):
        self.c.execute("""CREATE TABLE priceData (Time text,
        Price real)""")

    def insertData(self, priceDataObject):
        self.c.execute("INSERT INTO priceData VALUES (:Time, :Price)",
        {"Time": priceDataObject.time, "Price": priceDataObject.price})
    
    def showData(self):
        self.c.execute("SELECT * FROM priceData")
        self.c.fetchall()

    def closeDataBaseConnection(self):
        self.conn.cursor()

dataBaseManager = DataBaseManager()
dataBaseManager.createDataBase("bitcoin")
dataBaseManager.connectToDataBase("bitcoin.db")
#dataBaseManager.createTableInDataBase()
dataBaseManager.insertData(fakeData)
dataBaseManager.closeDataBaseConnection()
data = dataBaseManager.showData()
dataBaseManager.conn.close()
print(data)

