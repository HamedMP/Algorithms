import pandas as pd

data =pd.read_table('IntegerArray.txt')

test = []
for i in data['list']:
	test.append(i)

def merge_sort(tuple_arr_inv):
	array = tuple_arr_inv[0]
	inv = tuple_arr_inv[1]
	#print("inv is {}".format(inv))
	if len(array)<2:
		return array, inv
	else:
		half = len(array)/2
		#print("Half {}".format(half))
		left = array[0:half]
		right = array[half:len(array)]
		left_arr, left_inv = merge_sort((left, inv))
		right_arr, right_inv = merge_sort((right, inv))
		inversion = left_inv + right_inv 
		return merge(left_arr, right_arr, inversion)


def merge(left_arr, right_arr, inversion):
	left = left_arr
	right = right_arr
	merged_array = []
	n = len(left) + len(right)
	#print("N is {}".format(n))
	l = 0
	r = 0
	for i in range(0,n):
		#print("{} of {}".format(i, n-1))
		#print(merged_array)
		#if all the indexes of one array are used
		if l == len(left):
			for j in range(i,n):
				merged_array.append(right[r])
				r = r + 1
			break
		if r == len(right):
			for j in range(i,n):
				merged_array.append(left[l])
				l = l + 1
			break
		#comparing arrays
		if left[l] < right[r]:
			merged_array.append(left[l])
			l = l + 1
		else:
			merged_array.append(right[r])
			inversion = inversion + (len(left_arr) - l) #first array - index offirst array
			r = r + 1
	return (merged_array, inversion)


print(merge_sort((test, 0))[1])



