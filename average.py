#!/usr/bin/env python3
from __future__ import print_function, division
import sys
import statistics

with open(sys.argv[1], 'r') as f:
    print(statistics.mean(map(float, f.readlines())))

