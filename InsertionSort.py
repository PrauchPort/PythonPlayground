a_list = [6, 5, 3, 1, 8, 7, 2, 4]


def InsertionSort(list):
    unsortedList = list
    back = 1
    for i in range(1, len(unsortedList)):
        while (unsortedList[i] < unsortedList[i-back] and i-back >= 0):
            back += 1
        unsortedList.insert(i-back+1, unsortedList[i])
        del unsortedList[i+1]
        back = 1
    return unsortedList

print(a_list)
print(InsertionSort(a_list))

