#Task 1
def arithmetic(num):
    if not num:
        raise ValueError("List is empty")
    
    total_sum = sum(num)
    count = len(num)
    mean = total_sum / count
    return mean

num = [1, 2, 3, 4, 5]
print(arithmetic(num)) 


#Task 3

def remove_duplicates(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)

    return list2
list3 = [5, 17, 88, 23, 5 ,9]
print(remove_duplicates(list3))