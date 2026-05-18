#q1
def remove_duplicate(lst):
    return list(set(lst))

print(remove_duplicate([1, 2, 2, 3, 1, 4, 3]))

#q2
def count_unique(lst):
    count = 0
    lst = set(lst)
    for num in lst:
        count += 1
    return count

print(count_unique([1, 2, 2, 3, 1, 4]))

#q3
def common_element(lst1:list, lst2:list):
    lst3 = set(lst1) & set(lst2)
    return list(lst3)

print(common_element([1, 2, 3, 4] ,[3, 4, 5, 6]))

#q4
def only_one(lst1:list, lst2:list):
    lst3 = set(lst1).symmetric_difference(set(lst2))
    return list(lst3)
print(only_one([1, 2, 3, 4] ,[3, 4, 5, 6]))

#q5
def is_subset(lst1, lst2):
    flag = True
    for item in set(lst1):
        if item not in lst2:
            flag = False
    return flag

print(is_subset([1, 2, 6], [1, 2, 3, 4, 5]))

#q6
def unique_characters(string):
    flag = True
    set_string = set(string)
    if len(set_string) != len(string):
        flag = False
    return flag

print(unique_characters("abcdef"))

#q7
def first_repeated_element(lst):
    seen = set()

    for item in lst:
        if item in seen:
            return item
        seen.add(item)

    return None

print(first_repeated_element([1, 2, 3, 2, 4, 1]))


#q8
def distinct_words(string: str):
    distinct_word = set()
    for word in string.split():
        if not word in distinct_word:
            distinct_word.add(word.lower())
    return len(distinct_word)

print(distinct_words("The cat and the dog and the bird"))

#q9
def pair_sum_exists(lst, target):
    seen_numbers = set()
    for num in lst:
        complement = target - num
        if complement in seen_numbers:
            return True
        else:
            seen_numbers.add(num)
    return False

print(pair_sum_exists( [3, 1, 4, 7, 2], target = 6))


#q10
def sym_diff(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    lst3 = []

    for num in lst1:
        if num not in lst2:
            lst3.append(num)

    for num in lst2:
        if num not in lst1:
            lst3.append(num)

    return sorted(lst3)

print(sym_diff([1, 2, 3, 4], [3, 4, 5, 6]))

