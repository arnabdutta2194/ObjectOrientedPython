class MultiFunctionDevice:
    def print(self):
        return "Printing..."

    def scan(self):
        return "Scanning..."

    def fax(self):
        return "Faxing..."  # Not all clients need faxing

#-- Issue: The MultiFunctionDevice class has methods that not all users will use (like fax). 
# Clients that only need printing or scanning are forced to implement unnecessary functionality, violating ISP.

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

#-- Improvement: By creating separate interfaces (Printer and Scanner), clients only implement what they need. 
# This adheres to ISP by preventing clients from being forced to depend on unused methods.


