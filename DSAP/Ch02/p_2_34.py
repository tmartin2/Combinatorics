import os
import string
import itertools as it
import matplotlib.pyplot as plt

__author__ = 'Trevor Martin'


class AlphabeticFreq:

    __slots__ = ['_document']

    def __init__(self, document):

        if (type(document) != str) or (document[-4:] != '.txt'):
            raise TypeError('The document must be of type str and must end with .txt')
        
        self._document = document

    def frequency(self):

        with open(self._document, 'r') as file:
            lines = file.readlines()

            # replace '\n' with ''
            lines = [elt.replace('\n', '') for elt in lines]

            # remove punctuation
            lines = [elt.translate(str.maketrans('', '', string.punctuation)) for elt in lines]

            chars = list(it.chain.from_iterable([list(elt) for elt in lines]))

            # remove spaces
            chars = list(filter(lambda elt: elt != ' ', chars))

            # make lowercase
            chars = [elt.lower() for elt in chars]

            freq = dict(zip(string.ascii_lowercase, [0]*26))
            
            for elt in chars:
                freq[elt] += 1

            indices = list(range(0,260,10))

            plt.bar(x=indices, height=freq.values(), tick_label=list(freq.keys()), color='red')
            plt.title(f'Letter Frequency in {self._document}')
            plt.xlabel('Letters of the Alphabet')
            plt.ylabel('Numbers of Occurrences')
            plt.show()
            


if __name__ == '__main__':
    document = 'test.txt'
    freq_finder = AlphabeticFreq(document)
    freq_finder.frequency()
