list1=[4, 6, 9, 3, 1]
def manual_min(list1):

    min_value = list1[0]
    for num in list1[1:]:
        if num < min_value:
            min_value = num
    return min_value

manual_min(list1)