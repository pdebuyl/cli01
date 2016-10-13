#!/usr/bin/env python3
from __future__ import print_function, division
import sys

print("Number of arguments:", len(sys.argv)-1)
print(*sys.argv[1:])

