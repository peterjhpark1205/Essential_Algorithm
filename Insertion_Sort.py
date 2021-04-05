# Insertion Sort

# Insertion Sort is one of the sorting algorithms
# It starts at the second place of the list and keep compare with values which are in front of the pointed value, while the pointer moves toward the end of the list.
# Durting the process the pointed value is inserted to the right place among the values in front of the pointed value.




def insertion_sort(list):

    for index in range(1, len(list)):
        for index2 in range(0, index):
            if list[index] < list[index2]:
                list[index], list[index2] = list[index2], list[index]
            else:
                pass

    return list
