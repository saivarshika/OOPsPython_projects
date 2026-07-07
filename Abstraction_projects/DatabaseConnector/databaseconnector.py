from abc import ABC, abstractmethod

class DBConnection(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass


class MySQLConnection(DBConnection):

    def connect(self):
        print("Connected to MySQL Database")

    def execute(self, query):
        print("Executing on MySQL:", query)


class SQLiteConnection(DBConnection):

    def connect(self):
        print("Connected to SQLite Database")

    def execute(self, query):
        print("Executing on SQLite:", query)


mysql = MySQLConnection()
sqlite = SQLiteConnection()

mysql.connect()
mysql.execute("SELECT * FROM students")

print()

sqlite.connect()
sqlite.execute("SELECT * FROM employees")