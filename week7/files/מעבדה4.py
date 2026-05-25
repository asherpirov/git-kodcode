def create_grades_file(filename):
    students = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68]),
    ]
    with open(filename, "w", encoding="utf-8") as f:
        for name, grade in students:
            f.write(name + "," + str(grade[0]) +","+ str(grade[1]) +","+ str(grade[2]) +"\n")


create_grades_file("grades.txt")


def calculate_averages(filename):

    averages = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
           sum_grade = 0
           line =  line.strip().split(",")
           name = line[0]
           grades = line[1:]
           for grade in grades:
                sum_grade += int(grade)
           avg = sum_grade / 3
           averages[name] = avg

    return averages

results = calculate_averages('grades.txt')
for name, avg in results.items():
    print(f'{name}: {avg:.1f}')


def save_results(averages, output_filename):
    """
    :filename_output כותבת לקובץ
    שורה ראשונה: כותרת
    שורות הבאות: שם וממוצע, ,ממויין ממגבוה לנמוך
    """
    flipped_list = []
    for name, avg in averages.items():
        flipped_list.append((avg, name))

    sorted_averages = sorted(flipped_list, reverse=True)

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("=== Student Results ===\n")

        for i, (avg, name) in enumerate(sorted_averages):
            f.write(f"{i+1}. {name}: {avg:.1f}\n")
    max_grade = 0


averages = calculate_averages('grades.txt')
print(save_results(averages, 'results.txt'))


def append_statistics(filename, results):
    if not results:
        return

    averages_list = list(results.values())
    total_students = len(results)
    class_avg = sum(averages_list) / total_students
    max_avg = max(averages_list)
    min_avg = min(averages_list)

    best_student = ""
    worst_student = ""
    passed_count = 0

    for name, avg in results.items():
        if avg == max_avg:
            best_student = name
        if avg == min_avg:
            worst_student = name

        if avg >= 60:
            passed_count += 1

    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n=== Statistics ===\n")
        f.write(f"Class average: {class_avg:.1f}\n")
        f.write(f"Highest: {best_student} {max_avg:.1f}\n")
        f.write(f"Lowest: {worst_student} {min_avg:.1f}\n")
        f.write(f"Passing (>=60): {passed_count}/{total_students}\n")

append_statistics("results.txt", results)



