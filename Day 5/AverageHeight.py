student_heights = input("Input your height: ").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
for height in student_heights:
    total += height
print(f"Total height = {total}")

total_students = 0
for student in student_heights:
    total_students += 1
print(f"Number of students = {total_students}")

average = total / total_students
print(f"The average height is = {average}")

# can simply use sum and ave