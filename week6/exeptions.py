#q1
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None
print(safe_int(1))

#q2
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"
print(safe_divide(10,0))

#q3
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing"

print(get_value({"a": 1}, "b"))

#q4
def parse_ints(values):
    int_lst = []
    for num in values:
        try:
            int_lst.append(int(num))
        except ValueError:
            continue

    return int_lst

print(parse_ints(["1", "2", "x", "3", "y"]))

#q5
def set_age(age):
    if 0 > age or age > 150:
        raise ValueError
    return age


#q6
def retry(func, n):
    for i in range(n):
        try:
            return func()
        except Exception:
            if i == n-1:
                raise

#q7
def count_errors(funcs):
    count = 0
    for func in funcs:
        try:
            func()
        except Exception:
            count += 1
    return count

print(count_errors( [lambda: 1, lambda: 1/0, lambda: int("x"), lambda: 2]))

#8
def load_config(path):
    try:
       with open(path) as f:
          count =  int(f.readline())
          return count
    except Exception as e:
        raise RuntimeError("failed to load config") from e
print(load_config("test.txt"))

