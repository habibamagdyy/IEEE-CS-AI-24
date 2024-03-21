import collections
import math

def probabilitydistribution(data):
    frequency = collections.Counter(data)
    totalvalues = len(data)

    prob_dist = {value: count / totalvalues for value, count in frequency.items()}
    return prob_dist

data = input("Enter a list of values separated by spaces: ").split()
data = [int(x) for x in data]
prob_dist = probabilitydistribution(data)
for value, prob in prob_dist.items():
    print(f"Value: {value}, Probability: {prob:.1f}")