import pandas as pd
import numpy as np

array = pd.read_csv('QuickSort.csv')
array = np.array(array).flatten()
type(array)
len(array)



counter = 0

def partition(array, l, r):
	pivot = array[l]
	i = l + 1
	for j in range(l+1,r):
		if array[j] < pivot:
			swap(array, i, j)
			i = i + 1
	swap(array, l, i-1)
	return i-1

def choosePivot(A, begin, end):
	#return begin
	#return end - 1
	return getMedian(A, begin, end)

def QuickSort(A, begin, end):
	global counter
	#print(begin)
	if end - begin == 0:
		return 
	p = choosePivot(A, begin, end)
	swap(A, p, begin)
	i = partition(A, begin, end)

	counter = counter + (i - begin)
	QuickSort(A, begin, i)

	counter = counter + (end - (i+1))
	QuickSort(A, i+1, end)

def swap(array, idx1, idx2):
	temp = array[idx1]
	array[idx1] = array[idx2]
	array[idx2] = temp

def getMedian(array, begin, end):
	if (end-begin) % 2 != 0:
		middle_index = ((end-begin)/2)+begin
	else:
		middle_index = ((end-begin)/2)+begin - 1
	first_value = array[begin]
	last_value = array[end-1]
	middle_value = array[middle_index]

	median = np.median([first_value, middle_value, last_value])
	if median == first_value:
		return begin
	elif median == last_value:
		return end - 1
	else:
		return middle_index


#array = array[0:10]
#print(array)

array = [2,3,1,4]
QuickSort(array, 0, len(array))
print array
print counter




