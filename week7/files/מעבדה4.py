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

with open("results.txt") as f:
    print(f.read())

