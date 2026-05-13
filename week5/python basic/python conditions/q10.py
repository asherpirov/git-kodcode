score = int(input("Enter score (0-100): "))

grade = ("A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F")))

print(grade)