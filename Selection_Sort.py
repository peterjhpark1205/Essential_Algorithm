# Selection Sort

# 왜.. 왜!!! 값이 계속 삐끗하는 것인가... 해결이 시급하도다.. 밥먹고 


def selection_sort(list):

    for index in range(len(list) - 1):
        temp = index
        for index2 in range(index, len(list) - 1):
            if list[index2] < list[index2 + 1]:
                temp = index2
            else:
                temp = index2 + 1
        list[index], list[temp] = list[temp], list[index]

    return list
