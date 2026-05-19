count = 0
def bump():
    global count
    count += 1


def value():
    return count

bump()
bump()
bump()
print(value())