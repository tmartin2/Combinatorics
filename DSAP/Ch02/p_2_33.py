__author__ = 'Trevor Martin'


class Polynomial:
    
    __slots__ = ['_polynomial']

    def __init__(self, polynomial):

        if type(polynomial) != list:
            raise TypeError('The polynomial must be a list format')

        if len(polynomial) == 0:
            raise TypeError('The polynomial must contain at least one term')

        for elt in polynomial:
            if type(elt) != int:
                raise TypeError('Each element of the polynomial list must be an integer')

        self._polynomial = polynomial

    def derivative(self):

        dx = ''
        degree = len(self._polynomial) - 1
        
        if degree == 0:
            return f'The derivate of the polynomial {self._polynomial} is 0'
        
        for index, elt in enumerate(self._polynomial):
            if index+1 == len(self._polynomial):
                dx += ' + 0'
            else:
                if elt*degree == 0:
                    pass
                if elt > 0 and index != 0:
                    dx += ' + '+str(elt*degree)+'x**'+str(degree-1)
                if elt < 0 and index != 0:
                    dx += ' - '+str(abs(elt*degree))+'x**'+str(degree-1)
                if index == 0:
                    dx += str(elt*degree)+'x**'+str(degree-1)
                degree -= 1
        return f'The derivate of the polynomial {self._polynomial} is {dx}'
            

if __name__ == '__main__':
    polynomial = Polynomial([1,2]).derivative()
    polynomial1 = Polynomial([-4,-6,9,10,2]).derivative()
    polynomial2 = Polynomial([4,4,4,4]).derivative()
    polynomial3 = Polynomial([27,232,6]).derivative()
    print(f'{polynomial}\n{polynomial1}\n{polynomial2}\n{polynomial3}')
    #polynomial = Polynomial([])
    #polynomial = Polynomial(['a',3,2,1])
    #polynomial = Polynomial('1234')
        
