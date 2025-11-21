country = input()
ured = input()
grade_difficulty = 0
grade_execution = 0
max_grade = 20

if ured == 'ribbon':

    if country == 'Russia':
        grade_difficulty = 9.100
        grade_execution = 9.400
    elif country == 'Bulgaria':
        grade_difficulty = 9.600
        grade_execution = 9.400
    elif country == 'Italy':
        grade_difficulty = 9.200
        grade_execution = 9.500

elif ured == 'hoop':

    if country == 'Russia':
        grade_difficulty = 9.300
        grade_execution = 9.800
    elif country == 'Bulgaria':
        grade_difficulty = 9.550
        grade_execution = 9.750
    elif country == 'Italy':
        grade_difficulty = 9.450
        grade_execution = 9.350

elif ured == 'rope':

    if country == 'Russia':
        grade_difficulty = 9.600
        grade_execution = 9.000
    elif country == 'Bulgaria':
        grade_difficulty = 9.500
        grade_execution = 9.400
    elif country == 'Italy':
        grade_difficulty = 9.700
        grade_execution = 9.150

total_grade = grade_difficulty + grade_execution
point_needed = max_grade - total_grade
protzent_needed = (point_needed / 20) * 100

print(f'The team of {country} get {total_grade:.3f} on {ured}.')
print(f'{protzent_needed:.2f}%')