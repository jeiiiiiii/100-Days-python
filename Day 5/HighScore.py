student_scores = input("Scores here: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
highscore = 0
for score in student_scores:
    if score > highscore:
        highscore = score
        
print(f"The highest score is: {highscore}")

#Can simply use max
