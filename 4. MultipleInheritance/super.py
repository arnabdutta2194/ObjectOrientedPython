class Animal:
    @classmethod
    def description(cls):
        return "An Animal"

class Bird(Animal):
    @classmethod
    def description(cls):
        s = super()
        print(s)
        return super().description() + " With Wings"

class Flamingo(Bird):
    @classmethod
    def description(cls):
        return super().description() + " and fabulous pink feathers"


s = Flamingo()
print(s.description())