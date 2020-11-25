from itertools import groupby

# Given a list (students) of dictionaries (name, grade):
sort_by_grades = [
    {'name': name, 'grade': grade} for name, grade in zip(
        ['Jane', 'John', 'Mary', 'Gina', 'Peter'], ['A', 'A', 'C', 'B-', 'C']
    )
]

# Print our list:
for student in sort_by_grades:
    print(student)


def get_grades(students): return students['grade']  # get all grades


# Sort class data by grades:
sort_by_grades.sort(key=get_grades)

print('sort_by_grades:')
for student in sort_by_grades:
    print(student)

# Group class data by grades:
print('#' * 40)

group_by_grades = groupby(sort_by_grades, get_grades)

for grade, students in group_by_grades:
    print(f'{grade} students:')
    for student in students:
        print(list(student.values())[0])

