__author__ = 'Trevor Martin'

class Flower:
    
    __slots__ = ['_name', '_num_petals', '_price']
    
    def __init__(self, name, num_petals, price):
        if type(name) != str:
            raise TypeError('The flower name should be a string')

        if type(num_petals) != int:
            raise TypeError('The number of petals in a flower should be an integer')

        if type(price) != float:
            raise TypeError('The price should be a float')

        self._name = name
        self._num_petals = num_petals
        self._price = price

    def set_name(self, new_name):
        if type(new_name) != str:
            raise TypeError('The flower name should be a string')
        self._name = new_name

    def get_name(self):
        return self._name

    def set_petals(self, new_petals):
        if type(new_petals) != int:
            raise TypeError('The number of petals in a flower should be an integer')
        self._num_petals = new_petals

    def get_petals(self):
        return self._num_petals

    def set_price(self, new_price):
        if type(new_price) != float:
            raise TypeError('The price should be a float')
        self._price = new_price

    def get_price(self):
        return self._price

if __name__ == '__main__':
    my_flower = Flower('Tulip', 6, 14.00)
    print(my_flower.get_name())
    print(my_flower.get_petals())
    print(my_flower.get_price())
    my_flower.set_name('Daisy')
    my_flower.set_petals(4)
    my_flower.set_price(69.420)
    print(my_flower.get_name())
    print(my_flower.get_petals())
    print(my_flower.get_price())
    #my_flower.set_name(1)
    #my_flower.set_petals(1.0)
    #my_flower.set_price(1)
    #my_flower02 = Flower(10.98, 'Dandelion', 'fourteen')
    
