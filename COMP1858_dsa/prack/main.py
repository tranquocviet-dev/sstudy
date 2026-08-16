num_list = [3, 6, 9, 12]
# 1
def home_made_reverse(nlist):
	newlist = []
	for i in range(len(nlist) -1, -1, -1):
		newlist.append(nlist[i])
	return newlist

modded_num_list = home_made_reverse(num_list)
print(modded_num_list)

# 2
def hm_selection_sort(arr):
	n = len(arr)
	for i in range(n-1):
		min_index = i
		for j in range(i+1, n):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr, reverse=False):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1]) != reverse:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
arr1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr1)
print("Sorted array (ascending):", arr1)

arr2 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr2, reverse=True)
print("Sorted array (descending):", arr2)
