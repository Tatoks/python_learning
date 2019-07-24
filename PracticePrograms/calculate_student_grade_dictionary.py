# Calculate grade using nested dictionaries

student_record = {1000: {'name': 'A', 'M': 50, 'P': 60, 'C': 70}, 1001: {'name': 'B', 'M': 55, 'P': 65, 'C': 75}}

for key, value in student_record.items():
    print('****************************')
    print('ID: ' + str(key))
    total_marks = 0
    for k1, v1 in value.items():
        if k1.casefold() == 'name':
            print(k1.capitalize() + ': ' + v1)
        if (k1 == 'M') or (k1 == 'P') or (k1 == 'C'):
            total_marks = total_marks + v1
    average_scre = total_marks / 3
    if average_scre >= 75:
        print('Grade A')
    elif average_scre >= 65 and average_scre < 75:
        print('Grade B')
    else:
        print('Grade C')
print('****************************')
