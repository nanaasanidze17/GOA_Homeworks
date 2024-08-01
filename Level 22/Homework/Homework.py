#Task 2 

def manual_min(list1):

    min_value = list1[0]
    for num in list1[1:]:
        if num < min_value:
            min_value = num
    return min_value

list1=[4, 6, 9, 3, 1]
manual_min(list1)

print(manual_min(list1))

#Task 3
def manual_max(list2):

    max_value = list2[0]
    for num in list2[1:]:
        if num > max_value:
            max_value = num
    return max_value

list2=[8, 25, 99, 23, 11]
manual_max(list2)

print(manual_max(list2))

#Task 4
def manual_len(listn):
    len = 0
    for item in listn:
        len += 1
    return len

listn=[4, 2, 23, 7]
manual_len(listn)

print(manual_len(listn))


#Task 5
def manual_sum(list3):
    total = 0
    for num in list3:
        total += num
    return total
list3=[1, 2, 3, 4, 5, 6]
manual_sum(list3)

print(manual_sum(list3))


