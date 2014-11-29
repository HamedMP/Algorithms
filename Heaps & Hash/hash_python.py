#2-SUM Problem
#find distinct x and y = t

import pandas as pd 
import numpy as np
import csv
from sys import argv
import operator

filename = argv[1]
file = open(filename, 'r')

#read in hash table
hash_table = {}
with open(filename,"r") as text:
  for line in text:
    new_line= line.strip().split()[0]
    hash_table[int(new_line)] = int(new_line)

print("Read in file")

def Two_Sum_hash(hash_table, list_of_targets):
  #checked = set()
  checked_t = set()
  #loop over each target t
  for t in list_of_targets:
    #find the pair that could match these
    for i in hash_table:
      j = t - i
      #print("{} and {} = {}".format(i,j, t))
      try:
        if i != j:
          hash_table[j]
          checked_t.add(t)
          break
      except:
        pass
  print(checked_t)
  print(len(checked_t))

def Two_Sum_take_ends(sorted_keys, list_of_targets):
    checked_t = set()
    list_of_targets = set(list_of_targets)
    for i in range(0,len(sorted_keys)):
      for j in reversed(range(len(sorted_keys))):
        t = sorted_keys[i] + sorted_keys[j]
        #print("{} and {} = {}".format(i,j, t))
        if i != j and t in list_of_targets:
            checked_t.add(t)
        if i == j:
            break
    return len(checked_t)

def Two_Sum_cut_list(sorted_keys, list_of_targets):
  #shorted the list initially
  new_max = list_of_targets[len(list_of_targets)- 1]
  new_min = list_of_targets[0]
  for i in sorted_keys:
    if i >= 0:
        min_positive= i
        break
  min_comb = sorted_keys[0] + sorted_keys[1]
  max_comb = min_positive + sorted_keys[len(sorted_keys)-1]
  if max_comb <= new_max:
    new_max = max_comb
  if min_comb >=  new_min:
    new_min = min_comb
  print("Target list from {} to {}".format(new_min, new_max))
  list_of_targets = set(range(new_min, new_max))
  sums = set()
  print("Checking total {}".format(len(sorted_keys)))
  for i in range(0,len(sorted_keys)-1):
    for j in range(i+1, len(sorted_keys)):
      #print("adding {}".format(sorted_keys[i] + sorted_keys[j]))
      sums.add(sorted_keys[i] + sorted_keys[j])
  sums_list = np.sort(list(sums))
  final_sums = [x for x in sums_list if x in list_of_targets]
  print(final_sums)
  return len(final_sums)


list_of_targets = range(-10000, 10001)
sorted_keys = sorted(hash_table.keys())

print("Begin Two Sum algorithm- ends")
output= Two_Sum_cut_list(sorted_keys, list_of_targets)
print("There are {} from the list".format(output))
print("Complete")

#print("Begin Two Sum algorithm")
#Two_Sum_hash(hash_table, list_of_targets)
#print("Complete")