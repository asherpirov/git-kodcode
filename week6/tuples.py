#q1
def sum_tpl(tpl):
    sum_of_tpl = 0
    for num in tpl:
        sum_of_tpl += num
    return sum_of_tpl

print(sum_tpl((1,2,3,4,5)))

#q2
def max_number(tpl):
    max_num = 0
    for num in tpl:
        if num > max_num:
            max_num = num
    return max_num

print(max_number((3, 7, 2, 8, 5)))

#q3
def count_num(tpl, value):
    count = 0
    for num in tpl:
        if num == value:
            count += 1
    return count

print(count_num((1, 2, 3, 2, 4, 2), 2 ))

#q4
def reverse_tpl(tpl: tuple):
    revs_tpl = ()
    for index in range(len(tpl)):
       revs_tpl = revs_tpl +(tpl[-1-index],)
    return revs_tpl
print(reverse_tpl((1,2,3,4)))

#q5
def swap_pairs(tpl: tuple):
    swp_tpl = ()
    for num in range(0, len(tpl), 2):
        a, b = tpl[num+1], tpl[num]
        swp_tpl += (a, b)
    return swp_tpl

print(swap_pairs((1,2,3,4,5,6)))


#q6
def max_and_min(tpl):
    max_num = 0
    min_num = 1
    for num in tpl:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return min_num, max_num

print(max_and_min((4,1,7,3,5)))

#q7
def distance(tpl_x, tpl_y):
    return (((tpl_x[0] - tpl_y[0]) ** 2) + ((tpl_x[1] - tpl_y[1]) ** 2)) ** 0.5
print(distance((0,0), (3,4)))

#q8
def marge_and_sort(tpl1, tpl2):
    return tuple(sorted(tpl1 + tpl2))
print(marge_and_sort( (3, 1, 4), (1, 5, 9)))

#q9
def frequency_table(tpl):
    new_tpl = ()
    for num in tpl:
        count = count_num(tpl, num)
        tpl1 = num, count
        if tpl1 in new_tpl:
            continue
        new_tpl += tpl1,
    return new_tpl
print(frequency_table(("a", "b", "a", "c", "b", "a")))


#q10
def rotate_lst(tpl, k):
    if k > len(tpl):
        k = k % len(tpl)
    return tpl[-k:]+ tpl[:-k]

print(rotate_lst( (1, 2, 3, 4, 5), 2))
