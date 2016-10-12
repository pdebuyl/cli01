#!/usr/bin/env python3
"""
Perform a simulation of a random walk. The walker can go left or right at every
step.
"""
from __future__ import print_function, division
import statistics

data = []
while True:
    try:
        x = input()
    except:
        break
    data.append(int(x))

print("Given", len(data), "data points")
print("The mean is              :", statistics.mean(data))
print("The standard deviation is:", statistics.stdev(data))
