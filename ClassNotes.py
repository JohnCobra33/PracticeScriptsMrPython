#"Create a script that takes 5 grades from a student through the keyboard (ranging from 0 to 10). Next, it should display all the grades, the average grade, the highest grade achieved, and the lowest grade."
grades = []

for i in range(1, 6):
    grade = int(input("Enter grade %d: " % i))

    while grade < 0 or grade > 10:
        print("The grade must be between 0 and 10.")
        grade = int(input("Enter grade %d: " % i))

    grades.append(grade)

print("Grades: ", end="")
for g in grades:
    print(g, " ", end="")

print("\nAverage grade: ", sum(grades) / len(grades))
print("Maximum grade: ", max(grades))
print("Minimum grade: ", min(grades))
