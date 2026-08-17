#let _ = ```typ
exec typst c "$0" --root "$(readlink -f "$0" | xargs dirname)/./"
⁠```
#set document(title: "", author: "user")
#set text(lang: "en")
#show link: set text(fill: blue, weight: 700)
#show link: underline
#outline()
#set heading(numbering: "1.")
#heading(level: 1)[Task 1] #label("org7f5901f")
The task is to not use reverse() or split (using [::\u{2d}1]) and
print an arr backwards. For this we use the \u{22}for\u{22} function and
loop the original arr backwards and add the value to the new arr.
#figure([#raw(block: true, lang: "python", "num_list = [3, 6, 9, 12]
def home_made_reverse(nlist):
	newlist = []
	for i in range(len(nlist) -1, -1, -1):
		newlist.append(nlist[i])
	return newlist

modded_num_list = home_made_reverse(num_list)
print(modded_num_list)")]) #label("org3c4a9f6")

#raw(block: false, "[12, 9, 6, 3]")
#heading(level: 1)[Task 2] #label("org9cf2f78")
The task is to implement a sorting algorithm, which i implemented
bubble sort.
#figure([#raw(block: true, lang: "python", "def bubble_sort(arr, reverse=False):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1]) != reverse:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr1)
print(\u{22}Sorted array (ascending):\u{22}, arr1)

arr2 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr2, reverse=True)
print(\u{22}Sorted array (descending):\u{22}, arr2)")]) #label("org2f727e1")

#raw(block: false, "Sorted array (ascending): [11, 12, 22, 25, 34, 64, 90]
Sorted array (descending): [90, 64, 34, 25, 22, 12, 11]")
