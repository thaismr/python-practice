from itertools import groupby

# Given a list (students) of dictionaries (name, grade):
students = [
    {'name': name, 'grade': grade} for name, grade in zip(
        ['Jane', 'John', 'Mary', 'Gina', 'Peter'], ['A', 'A', 'C', 'B-', 'C']
    )
]

# Print our list:
for student in students:
    print(student)


def get_grades(each_student): return each_student['grade']  # get grade for each student


# Sort class data by grades:
students.sort(key=get_grades)  # ATTENTION! Must sort students for 'groupby' to work!

print('Students sorted by grade:')
for student in students:
    print(student)

# Group class data by grades:
print('#' * 40)

group_by_grades = groupby(students, get_grades)

for grade, students in group_by_grades:
    print(f'{grade} students:')
    for student in students:
        print(list(student.values())[0])

