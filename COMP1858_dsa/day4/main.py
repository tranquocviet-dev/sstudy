lisst = [1, 2, 3, 4, 5, 6, 2, 2]
# Basic algorithm
# I. Search
# I.1 Find Max and Min
def findMaxMin(arr):
    curmax = arr[0]
    curmin = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < curmin:
            curmin = arr[i]
        elif arr[i] > curmax:
            curmax = arr[i]
    return curmax, curmin

print(findMaxMin(lisst))

# I.2 Find index of number in a list
# First solution: find first occurence of a number in a list and return None if found none
def findIndex(arr, key, first=True):
    n = len(arr)
    for i in range(len(arr)):
        rx = i if first else n - i - 1
        if arr[rx] == key:
            return rx
    return None

print(findIndex(lisst, 10))
# Second solution: Find all occurences of a number in a list, will return an empty list if found none
def findIndices(arr, key):
    n = len(arr)
    indices = None
    for i in range(n):
        if arr[i] == key:
            if indices is None:
                indices = []
            indices.append(i)
    return indices

findIndices(lisst, 2)


# 2. Arrange
arr2 = [2, 4, -3, 9, 10, 9]
# 2.1 Reverse a list
def ethicalReverse(arr):
    reversed_list = []
    # instead of looping from 0 to the end of the array which is len(arr), we loop from the end of array (len(arr) -1)
    for i in range (len(arr) -1, -1, -1):
        reversed_list.append(arr[i])
    return reversed_list

ethicalReverse(arr2)

print(arr2)
print(f'{ethicalReverse(arr2)}')

# 2.2 Partition a list based on criteria
# in this example i will partition based on whether the number is even or not
def partition(arr):
    even = []
    noteven = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            noteven.append(arr[i])
    return even, noteven

partition(arr2)
print(arr2)
print(f'{partition(arr2)}')


threshold = 4
# bidirectional approach
left = 0
right = len(arr2) - 1
while left < right:
    while arr2[left] < threshold:
        left += 1
    while arr2[right] >= threshold:
        right -= 1
    if left < right:
        arr2[left], arr2[right] = arr2[right], arr2[left]
        left += 1
        right -= 1
print(arr2)
