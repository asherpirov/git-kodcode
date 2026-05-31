from fastapi import FastAPI

grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}

app = FastAPI()

@app.get("/students")
def get_students():
    return grades

@app.get("/students/top")
def get_top_student():
    max_grade = 0
    max_student = ""
    for student in grades:
        if grades[student]["grade"] > max_grade:
            max_grade = grades[student]["grade"]
            max_student = grades[student]["name"]

    return {f"{max_student} : {max_grade}"}



@app.get("/students/average")
def get_students_average():
    count = 0
    for student in grades:
        count += grades[student]["grade"]
    avg = count / len(grades)
    return {"average_class" : avg}
        


@app.get("/students/count")
def get_students_count():
    return {"total_student":len(grades)}


@app.get("/students/{student_id}")
def get_student_by_name(student_id):
    if student_id in grades:
        return grades[student_id]
    return {"error": "the student not found"}


