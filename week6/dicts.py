#q1

def sum_value_dict(dct: dict):
    sum_of_val = 0
    for k in dct:
        sum_of_val+= dct[k]
    return sum_of_val

print(sum_value_dict({"a": 1, "b": 2, "c": 3}))

#q2

def max_key(dct: dict):
    max_val = 0
    maxi_key = ""
    for k in dct.keys():
        if dct[k] > max_val:
            max_val = dct[k]
            maxi_key = k
    return maxi_key
print(max_key({"a": 3, "b": 7, "c": 5}))

#q3

def count_char(string):
    cnt_dict = {}
    for c in string:
        if c in cnt_dict:
            cnt_dict[c] += 1
        else:
            cnt_dict[c] = 1
    return cnt_dict

print(count_char("banana"))

#q4
def invert_dict(dct: dict):
    new_dct = {}
    for k, v in dct.items():
      new_dct[v] = k
    return new_dct
print(invert_dict({"a": 1, "b": 2}))

#q5
def merge_dicts(dict1, dict2):
    for k in dict2:
        if dict2[k] in dict1:
            dict1[k] = dict2[k]
        else:
            dict1[k] = dict2[k]
    return dict1

print(merge_dicts({"a": 1, "b": 2}, {"b": 20, "c": 30}))

#q6
def filter_by_val(dct, threshold):
    new_dict = {}
    for k, v in dct.items():
        if threshold < v:
            new_dict[k] = dct[k]
    return new_dict
print(filter_by_val({"a": 1, "b": 5, "c": 3, "d": 8}, 3))

#q7
def grp_first_letter(lst: list):
    dct1 = {}
    for i in lst:
        key = i[0]
        if key in dct1:
            dct1[key] += [i]
        else:
            dct1[key] = [i]
    return dct1
print(grp_first_letter( ["apple", "ant", "banana", "berry", "cherry"]))

#q8
def word_count(string):
    cnt_dict = {}
    for word in string.split():
        if word in cnt_dict:
            cnt_dict[word] += 1
        else:
            cnt_dict[word] = 1
    return cnt_dict

print(word_count("the cat sat on the mat"))

#q9

def common_key(dict1, dict2):
    key_lst = []
    for key in dict2:
        if key in dict1:
            key_lst.append(key)
    return sorted(key_lst)
print(common_key( {"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7}))

#q10
def most_frequent_value(dct: dict):
    dict1 = {}
    for k, v in dct.items():
        if v in dict1.values():
            dict1[v] += 1
        else:
            dict1[v] = 1
    maxi = 0
    maxi_val = None

    for k, v in dict1.items():
        if v > maxi:
            maxi = v
            maxi_val = k
    return maxi_val

print(most_frequent_value( {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}))







