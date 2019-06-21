def SelectionSort(list):
    unsortedList = list
    index = 0
    for i in range(len(unsortedList)):
        indexMin = index
        for j in range (index, len(unsortedList)):
            if unsortedList[j] < unsortedList[indexMin]:
                indexMin = j
        unsortedList[indexMin], unsortedList[index] = unsortedList[index], unsortedList[indexMin]
        index = index + 1
    return unsortedList



a_list = [10, 12, 6, 9, 3, 5, 4, 8, 7]

print(SelectionSort(a_list))
