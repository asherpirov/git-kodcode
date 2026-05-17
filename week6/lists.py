#q1
def sum_of_list(lst):
    sum_of_lst = 0
    for num in lst:
        sum_of_lst += num
    return sum_of_lst

print(sum_of_list([1,5,3,4,5]))

#q2
def max_element(lst):
    max_num = 0
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(max_element([1,7,3,4,5]))

#q3
def count_num(lst, value):
    count = 0
    for num in lst:
        if num == value:
            count += 1
    return count

print(count_num([1,7,5,5,5], 5))

#q4
def reverse_list(lst):
    reverse_lst = []
    for i in range(len(lst)):
        reverse_lst.append(lst[-1-i])
    return reverse_lst

print(reverse_list([1,2,3,4,5]))


#q5
def remove_duplicates(lst):
    non_duplicate_lst = []
    for num in lst:
        if num in non_duplicate_lst:
            continue
        else:
            non_duplicate_lst.append(num)
    return non_duplicate_lst

print(remove_duplicates( [1, 2, 2, 3, 1, 4, 3]))

#q6
def second_largest_num(lst):
    second_max = 0
    max_num = 0
    for num in lst:
        if num > max_num:
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max


print(second_largest_num([4, 1, 7, 7, 6, 5]))

#q7
def merge_lists(lst1, lst2):
    lst3 = sorted(lst1 + lst2)
    return lst3

print(merge_lists([1,3,5], [2,4,6]))

#q8
def rotate_lst(lst, k):
    if k > len(lst):
        k = k % len(lst)
    lst1 = lst[:-k]
    lst2 = lst[-k:]
    return lst2 + lst1
print(rotate_lst([1,2,3,4,5], 7))





