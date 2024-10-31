student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for students in student_scores:
    score = student_scores[students]
    
    if score >= 91 :
        student_grades[students] = ("Outstanding")
    elif score >= 81:
        student_grades[students] = ("Exceeds Expectations")
    elif score >= 71:
        student_grades[students] = ("Acceptable")
    else:
        student_grades[students] = ("Fail")
        
print(student_grades)