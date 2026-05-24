import os

sentences_lst = ["\n15-01-2024: היה יום עמוס בפרויקט","\n16-01-2024: P-Pyth-ב Fil Handling על",
                 "\n17-01-2024: השלמתי את התרגיל הראשון!\n"]
with open("diary.txt", "w", encoding="utf-8") as f:
    f.writelines(sentences_lst)
    print("היומן נוצר בהצלחה!")

with open("diary.txt", "r",encoding="utf-8") as f:
    print(f.read())

def add_entry(filename, date, content):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{date}: {content}\n")


add_entry("diary.txt", "18-01-2024", "יום נפלא - סיימתי את התרגיל הראשון")

with open("diary.txt", "r",encoding="utf-8") as f:
    print(f.read())

def safe_read_diary(filename):
       if os.path.exists(filename):
            return True
       else:
           print("file not found")
           return False


def search_diary(filename, keyword):
    keyword_list = []
    if safe_read_diary(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if keyword in line:
                    keyword_list.append(line.strip())
    return keyword_list

print(search_diary("diary.txt", "יום"))



