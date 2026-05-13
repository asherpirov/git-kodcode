def manage_students(names, grades, new_name, new_grade):
    # validation
    is_valid_name(new_name)
    is_valid_grade(new_grade)


    # add student
    grades.append(new_grade)

    # calculate stats
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

    # print report
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

    # save to file
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")
    return names, grades


def is_valid_name(new_name):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
    return True

def is_valid_grade(new_grade):
    if new_grade <= 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return False
    return True

