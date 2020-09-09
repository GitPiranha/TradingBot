import sqlite3
from priceData import PriceData


# Create fake data
fakeData = PriceData("2020-10-24", 20000.142)

class DataBaseManager:
    """
        This class creates and manages the priceData database
    """

    def createDataBase(self, dataBaseName):
        self.conn = sqlite3.connect(dataBaseName + ".db")
    

    def connectToDataBase(self, dataBaseNameToConnectTo):
        self.conn = sqlite3.connect(dataBaseNameToConnectTo)
        self.c = self.conn.cursor()


    def createTableInDataBase(self):
        try:
            self.c.execute("""CREATE TABLE IF NOT EXISTS priceData (Date text,
            Price real);""")
        except:
            print("Error while creating table")
        

    def insertData(self, dataObject):
        sql = ''' INSERT INTO priceData(Date, Price)
              VALUES(?,?) '''    
        # self.c.execute("INSERT INTO priceData VALUES (:Date, :Price)",
        # {"Date": priceDataObject.date, "Price": priceDataObject.price})
        # self.conn.commit()
        data = (str(dataObject.date), dataObject.price)

        self.conn = sqlite3.connect("bitcoin.db")
        self.c = self.conn.cursor()
        # Execute sql command and use data to fill table
        self.c.execute(sql, data) 
        self.conn.commit()


    def showData(self):
        self.c.execute("SELECT * FROM priceData")
        print(self.c.fetchall())


    def closeDataBaseConnection(self):
        self.conn.cursor()

dataBaseManager = DataBaseManager()
dataBaseManager.createDataBase("bitcoin")
dataBaseManager.connectToDataBase("bitcoin.db")
dataBaseManager.createTableInDataBase()
#dataBaseManager.insertData(fakeData)

dataBaseManager.closeDataBaseConnection()
data = dataBaseManager.showData()
dataBaseManager.conn.close()
print(data)

