def recursionMax(list, i=0):
    length = len(list)
    if i == length - 1:
        return list[i]
    max = recursionMax(list, i + 1)
    return list[i] if list[i] > max else max


def recursionMaxRedo(arr, start, end):
    if start == end:
        return end, end
    else:
        max, min = recursionMaxRedo(arr, start + 1, end)
        if arr[start] > arr[max]:
            max = start
        if arr[start] < arr[min]:
            min = start
        return max, min
if __name__ == "__main__":
    newarr = [10, 25, 15, 20]
    print(recursionMax(newarr))
    print(recursionMaxRedo(newarr, 0, len(newarr)-1))
