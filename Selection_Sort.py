# Selection Sort

# 설명: 리스트에서 최솟값을 찾아 맨 앞으로 보낸다. 한번 수행하면 index를 다음으로 옮겨가 거기서부터의 최솟값을 맨 앞에서 그 다음 자리(index가 있는자리)에 놓는다.

# 잘못된 코드: 계속 index2를 따라가면 min값을 찾지 못한다. 즉 '내가 갖고 있는 값(기준점)'을 잡아줘야 한다.
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



# 수정된 코드
def selection_sort(list):

    for index in range(len(list) - 1):
        temp = index
        for index2 in range(index, len(list) - 1):
            if list[temp] < list[index2 + 1]:
                temp = temp
            else:
                temp = index2 + 1
        list[index], list[temp] = list[temp], list[index]

    return list
