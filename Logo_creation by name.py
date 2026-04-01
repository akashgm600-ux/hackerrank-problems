import math
import os
import random
import re
import sys
import collections

if __name__ == '__main__':
    s = input("company name: ")
    x = sorted(s.strip())
   
#print(x)
    count = collections.Counter(x).most_common(3) 
    for char , n in count:
        print(char , n)
        #creates a list of tuples with the most common characters and their counts, and prints them in the required format.