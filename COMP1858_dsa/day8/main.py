X = [2, 9, -2, 5, 1, 13, 15, 4, 8, 2 , 3]
def selection_sort(arr, ascend=True):
	#copy the arr to a new arr in order not to break the old one
	newarr = arr.copy()
	#looping for len(arr)-1 times
	for a in range(len(newarr) - 1):
		# set a dummy index, then check and update the index to the lowest number of the arr
		index = a
		for b in range(a+1, len(newarr)):
			if (ascend and newarr[b] < newarr[index]) or (not ascend and newarr[b] > newarr[index]):
				index = b
		# updating the index of the lowst arr to "a"
		newarr[a], newarr[index] = newarr[index], newarr[a]
	return newarr
def bubble_sort(X, ascend=True):
	n = len(X)
	arr = X.copy()

	for i in range(n-1):
		for j in range(n-1, i, -1):
			if (ascend and arr[j] < arr[j-1]) or (not ascend and arr[j] > arr[j-1]):
				arr[j], arr[j-1] = arr[j-1], arr[j]
	return arr

def countingserach(X, ascend=True):
	

arr = selection_sort(X, False)
print(arr)


