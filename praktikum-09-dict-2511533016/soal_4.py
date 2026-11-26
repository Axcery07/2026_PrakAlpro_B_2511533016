students = input().split()
submitted = input().split()

submitted_set = set(submitted)
students_set = set(students)

submitted_count = len(students_set & submitted_set)
not_submitted = students_set - submitted_set

print("Submitted: ", submitted_count, "students")
print("Not Submitted: ", len(not_submitted), "students")

for student in students:
    if student not in submitted_set:
        print(student)