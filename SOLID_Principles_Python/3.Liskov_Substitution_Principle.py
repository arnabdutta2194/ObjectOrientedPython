class Bird:
    def fly(self):
        return "I can fly!"

class Sparrow(Bird):
    pass

class Ostrich(Bird):
    def fly(self):  # Violates LSP
        raise Exception("I can't fly!")


#-- Issue: Ostrich, which is a subtype of Bird, cannot substitute for Bird without causing errors. 
# This violates LSP, as it breaks the expected behavior of the base class.

from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "I can fly!"

class Sparrow(FlyingBird):
    pass

class Ostrich(Bird):
    def move(self):
        return "I can run!"
