# Bubble Sort is used for sorting values on the list
# It compares and swap list's value from the top and the bigger value goes behind the comparing value.
# Once the value is sorted this function compares the rest of the values on the list which are not sorted properly.
## Note to this function is eventually values are sorted in order of their scales, for example first value which sorted behind the list is the biggest value in that list.
## If the values are properly sorted in the first place, there are no values that are needed to be swaped.


#####PHASE#####
# 0. [2, 1, 3, 5, 4]
# 1. [1, 2, 3, 4, 5]
# 2. No need to swap → Break




def bubble_sort(list):
    swap = False
    for index in range(len(list) - 1):
        for index2 in range(len(list) - index - 1):
            if list[index2] > list[index2 + 1]:
                list[index2], list[index2 + 1] = list[index2 + 1], list[index2]
                swap = True
            else:
                pass
                swap = False
        if swap is False:
            break

    return list
        
  

