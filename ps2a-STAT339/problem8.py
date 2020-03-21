# Problem 8, Problem Set 2a
# Author: Trevor Martin
# Date Completed: 10 March 2020

from scipy.stats import randint
import matplotlib.pyplot as plt
import numpy as np


# independent discrete uniform random variable generator
def discrete_uniform():
    return np.random.randint(low=1, high=5, size=1)

trial_results = [int(discrete_uniform())+int(discrete_uniform()) for trial in range(10000)]

unique_results = set(list(trial_results))

t = list(trial_results) # shortened for utility

counts = [f'\nValue: {val}\nNumber: {t.count(val)}\nPercent Total: {t.count(val)/100}%\n\n' for val in unique_results]

print(*counts) 


#fig, ax = plt.subplots(1, 1)

# independent discrete uniform random variables X and Y
#low_X = 1
#high_X = 6
# mean, var, skew, kurt = randint.stats(x_low, x_high, moments='mvsk')
#x = np.arange(randint.ppf(0.01, low_X, high_X),
#              randint.ppf(0.99, low_X, high_X))
#low_Y = 1
#high_Y = 4
# mean, var, skew, kurt = randint.stats(low_Y, high_Y, moments='mvsk')
#y = np.arange(randint.ppf(0.01, low_Y, high_Y),
#             randint.ppf(0.99, low_Y, high_Y))

#ax.plot(x, randint.pmf(x, low_X, high_X), 'bo', ms=8)
#ax.plot(y, randint.pmf(y, low_Y, high_Y), 'bo', ms=8)
#ax.vlines(x, 0, randint.pmf(x, low_X, high_X), colors='b', lw=5, alpha=0.5)
#ax.vlines(y, 0, randint.pmf(y, low_Y, high_Y), colors='r', lw=5, alpha=0.5)
#plt.show()
