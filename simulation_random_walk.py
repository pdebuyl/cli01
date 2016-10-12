#!/usr/bin/env python3
"""
Perform a simulation of a random walk. The walker can go left or right at every
step.
"""
from __future__ import print_function, division

import sys
import random

n_steps = int(sys.argv[1])

x = 0
for i in range(n_steps):
    x = x - 1 + 2*random.randrange(2)
    print(x)

