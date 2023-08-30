#!/bin/python3

import math
import os
import random
import re
import sys


def is_weird(n):
    if n % 2 == 1:
      return True
    elif 2 <= n <= 5:
      return False
    elif 6 <= n <= 20:
      return True
    else:
      return False
  
def main():
    n = int(input())
    print("Weird" if is_weird(n) else "Not Weird")
  
if __name__ == '__main__':
    main()
