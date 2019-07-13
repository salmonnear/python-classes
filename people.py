class Person(self, name, age, favFood, coolness):
    
    def __init__(self, name, age, favFood, coolness=75):
        self.name = name
        self.age = age
        self.favFood = favFood
        self.coolness = coolness

    def sayHi(self):
        return print('Hi!')

    def greet(self, personToGreet):
        return print('Hi %d' %personToGreet)

    def complain(self):
        self.coolness -= 5





Sam = Person('Sam', 26, 'steak', 100)

sam.complain()