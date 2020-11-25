from itertools import groupby

# Given a list (students) of dictionaries (name, grade):
class_grades = [
    {'name': name, 'grade': grade} for name, grade in zip(
        ['Jane', 'John', 'Mary', 'Gina', 'Peter'], ['A', 'A', 'C', 'B-', 'C']
    )
]

# Print our list:
for student in class_grades:
    print(student)


def get_grades(students): return students['grade']  # get all grades


class_grades.sort(key=get_grades)
group_by_grades = groupby(class_grades, get_grades)

print(list(group_by_grades))

# Get students grade:
# grade = lambda
