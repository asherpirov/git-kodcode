def load_tasks(filename):
    """
    :dicts קוראת את הקובץ ומחזירה רשימה של
    [{'id': 1, 'status': 'PENDING', 'desc': 'ללמוד Python'}, ...]
    אם הקובץ לא קיים — מחזירה רשימה ריקה
    """
    tasks_lst = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                split_line = line.strip().split("|")
                task_dict = {"id": int(split_line[0]), "status": split_line[1], "desc": split_line[2]}
                tasks_lst.append(task_dict)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []

    return tasks_lst


def save_tasks(filename, tasks):
    """
    שומרת את רשימת המשימות לקובץ
    description|status|id :פורמט כל שורה
    """
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            task_id = task["id"]
            status = task["status"]
            desc = task["desc"]

            line = f"{task_id}|{status}|{desc}\n"
            f.write(line)

def add_task(filename, description):
    """
    :מוסיפה משימה חדשה עם
    מספר המשימה הבאה = ID -
    - status = 'PENDING'
    הפרמטר שניתן = description -
    """
    tasks = load_tasks(filename)
    last_task = tasks[-1]
    new_id = last_task["id"] + 1
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{new_id}|PENDING|{description}\n")


def complete_task(filename, task_id):
    """
    DONE-ל PENDING-מ id_task של משימה status משנה את
    לא קיים — מדפיסה הודעת שגיאה ID-אם ה
    """
    tasks = load_tasks(filename)

    task_found = False

    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = "DONE"
            task_found = True
            break
    if task_found:
        save_tasks(filename, tasks)
        print(f"Task {task_id} completed successfully.")
    else:
        print(f"Error: Task with ID {task_id} does not exist.")

def list_tasks(filename):
    """
    מציגה את כל המשימות בפורמט מסודר:
    [✓] 2 | לכתוב תרגיל 1
    [ ] 3 | לסיים את הפרויקט
    """
    tasks = load_tasks(filename)
    for task in tasks:
        if task["status"] == "DONE":
            status_icon = "[✓]"
        else:
            status_icon = "[]"
        print(f"{status_icon} {task['id']}|{task['desc']}")

def remove_tasks(filename, task_id):
    tasks = load_tasks(filename)

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"The task {task_id} removed")
            break
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            task_id = task["id"]
            status = task["status"]
            desc = task["desc"]

            line = f"{task_id}|{status}|{desc}\n"
            f.write(line)


def main():
    FILENAME = "tasks.txt"
    while True:
        print('\n=== To-Do List Manager ===')
        print('1. הצג משימות')
        print('2. הוסף משימה')
        print('3. סמן כהושלם')
        print("4. מחק משימה")
        print('5. יציאה')
        choice = input('בחירה: ')

        if choice == '1':
            list_tasks(FILENAME)
        elif choice == '2':
            desc = input('תיאור המשימה: ')
            add_task(FILENAME, desc)
            print('המשימה נוספה!')
        elif choice == '3':
            task_id = int(input('מספר משימה: '))
            complete_task(FILENAME, task_id)
        elif choice == "4":
            task_id = int(input('מספר משימה: '))
            remove_tasks(FILENAME, task_id)
        elif choice == '5':
            print('להתראות!')
            break
        else:
            print('בחירה לא תקינה')

if __name__ == '__main__':
    main()



















