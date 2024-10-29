class MySQLDatabase:
    def connect(self):
        return "Connected to MySQL"

class UserService:
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency on MySQLDatabase

    def get_user(self):
        return self.database.connect()
    
#-- Issue: UserService directly depends on MySQLDatabase, making it rigid. 
# Any change in the database implementation would require changes in UserService, violating DIP.

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"

class UserService:
    def __init__(self, database: Database):
        self.database = database

    def get_user(self):
        return self.database.connect()

#-- Improvement: UserService now depends on the Database abstraction rather than a concrete implementation. 
# This allows you to easily swap out the database implementation without modifying UserService, adhering to DIP.