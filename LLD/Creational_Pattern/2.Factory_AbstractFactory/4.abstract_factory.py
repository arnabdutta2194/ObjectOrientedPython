from abc import ABC,abstractmethod

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This Tea is delicious')

class Coffee(HotDrink):
    def consume(self):
        print('This Coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self,amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Preparing Tea with Amount {amount} ml')
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Preparing Coffee with Amount {amount} ml')
        return Coffee()
    
tea = TeaFactory().prepare(100)
print(tea.consume())

coffee = CoffeeFactory().prepare(200)
print(coffee.consume())