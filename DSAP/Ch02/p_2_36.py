import random
random.seed(10)

__author__ = 'Trevor Martin'


class Ecosystem:

    __slots__ = ['_initial_bears', '_initial_fish', '_len_river', '_river']

    def __init__(self, initial_bears, initial_fish, len_river):

        if type(initial_bears) != int or type(initial_fish) != int or type(len_river) != int:
            raise TypeError('The initial bears and fish as well as the river length must be integers')

        assert len_river >= (initial_bears+initial_fish), 'The length of the river must exceed the starting total of bears and fish combined' 
        
        self._initial_bears = initial_bears
        self._initial_fish = initial_fish
        self._len_river = len_river
        self._river = self.fill_river()
        
    def fill_river(self):
        river = [None]*self._len_river
        indices = list(range(self._len_river))
        random.shuffle(indices)
        for index in indices:
            if self._initial_bears == 0 and self._initial_fish != 0:
                choice = 0
                
            if self._initial_bears != 0 and self._initial_fish == 0:
                choice = 1
                
            if self._initial_bears == 0 and self._initial_fish == 0:
                break
            
            if self._initial_bears !=0 and self._initial_fish: 
                choice = random.randrange(0, 1)
                
            if choice == 1:
                river[index] = 'bear'
                self._initial_bears -= 1

            if choice == 0:
                river[index] = 'fish'
                self._initial_fish -= 1
                
        return river

    
    def course(self, time_steps):

        if type(time_steps) != int:
            raise TypeError('The time steps must be an integer value')

        print(f'INITIAL ECOSYSTEM: {self._river}')

        for life in range(time_steps):
            for index, val in enumerate(self._river):
            
                none_indices = [i for i, elt in enumerate(self._river) if elt == None]
            
                move = random.randrange(0,1)
                if move == 1:
                    position = index+1
                if move == 0:
                    position = index-1
            
                if val == 'fish' and self._river[position] == 'fish':
                    if len(none_indices) > 0:
                        choice = random.randint(0, len(none_indices)-1)
                        self._river[none_indices[choice]] = 'fish'
                if val == 'bear' and self._river[position] == 'bear':
                    if len(none_indices) > 0:
                        choice = random.randint(0, len(none_indices)-1)
                        self._river[none_indices[choice]] = 'bear'
                if val == 'bear' and self._river[position] == 'fish':
                    self._river[position] = None
                if val == 'fish' and self._river[position] == 'bear':
                    self._river[index] = None
            print(f'LIFETIME {life}: {self._river}')

if __name__ == '__main__':
    ecosystem = Ecosystem(5,18,23)
    ecosystem.course(3)
    
