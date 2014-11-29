import csv
import heapq
import math
import operator
from sys import argv

import numpy as np
import pandas as pd
import timeit

#median maintenance
def heap_median_maintenance(read_in):
    starting_list = []
    median = []
    for i in read_in:
        starting_list.append(i)
        #If it's the first element being read in, that is the median
        if len(starting_list) == 1:
            low_heap = heapq.nsmallest(len(starting_list), starting_list)
            high_heap = heapq.nlargest(len(starting_list)-1, starting_list)
        #if even then split half way
        elif len(starting_list)%2 ==0:
            low_heap = heapq.nsmallest(len(starting_list)/2, starting_list)
            high_heap = heapq.nlargest(len(starting_list)/2, starting_list)
        #if odd give the larger portion to low heap
        else:
            low_list_amount = int(math.ceil(float(len(starting_list))/2))
            high_list_amount = int(len(starting_list) - math.ceil(float(len(starting_list))/2))
            low_heap = heapq.nsmallest(low_list_amount, starting_list)
            high_heap = heapq.nlargest(high_list_amount, starting_list)
            #print("Low heap has {} and high heap has {}".format(len(low_heap), len(high_heap)))
        #print("Low heap {}".format(low_heap))
        #print("high heap {}".format(high_heap))
        #print("Median is {}".format(heapq.nlargest(1, low_heap)[0]))
        #append median from the largest element of the low_heap
        median.append(heapq.nlargest(1, low_heap)[0])
    return median

if __name__ == '__main__':
    filename = argv[1]
    file = open(filename, 'r')
    print("Reading in file {}".format(filename))
    #read in array
    read_in = []
    with open(filename,"r") as text:
      for line in text:
        new_line= line.strip().split()[0]
        read_in.append(int(new_line))
    print("Reading file completed")
    medians = heap_median_maintenance(read_in)
    print(np.sum(np.array(medians))%10000)


#timeit.timeit('import hash_median as hm; hm.heap_median_maintenance(range(0,10000))', number = 1)
#100 0.008532
#1000 0.9362
#10000 109.87