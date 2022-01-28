import numpy as np
import matplotlib.pyplot as plt


class Coin():

    #initializes coin with probability of heads p
    def __init__(self, p):
        self.p = p
    
    def flip(self, x):
        return int(x < self.p)
    
    def flip_coins(self, coins):
        return [self.flip(x) for x in coins]
    
    def flip_coins_times(self, experiment):
        return [self.flip_coins(x) for x in experiment]
    
    #returns array of results of flipping x coins, y times
    def flip_x_coins_y_times(self, x, y):
        experiment = np.random.rand(y, x)
        return self.flip_coins_times(experiment)

def choose(n, k):
    return np.math.factorial(n) / ( np.math.factorial(k) * np.math.factorial(n-k))

#returns array of expected values according to binomial distribution
def binomial(times, n, p):
    distribution = []
    for k in range(n):
        distribution.append(times * choose(n, k) * p**k * (1-p)**(n-k))
    return distribution

if __name__ == '__main__':
    coins = 20
    times = 1000
    p = 0.5
    c = Coin(p)
    data = c.flip_x_coins_y_times(coins,times)
    heads = np.matmul(data, [1]*coins) # array of number of heads for each trial
    freqs = [0]*coins
    for i in heads:
        freqs[i] += 1 # finds frequencies of each number of heads
    binomial = binomial(times, coins, p)
    random_trials = plt.plot(freqs, 'o')
    bin_dist = plt.plot(binomial)
    plt.legend(['random coin flips', 'binomial distribution'])
    plt.show()