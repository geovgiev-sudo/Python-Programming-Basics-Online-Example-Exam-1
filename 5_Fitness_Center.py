visitors = int(input())

back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0

for i in range(1, visitors + 1):
    activity = input()

    if activity == 'Back':
        back_counter += 1
    elif activity == 'Chest':
        chest_counter += 1
    elif activity == 'Legs':
        legs_counter += 1
    elif activity == 'Abs':
        abs_counter += 1
    elif activity == 'Protein shake':
        protein_shake_counter += 1
    elif activity == 'Protein bar':
        protein_bar_counter += 1

work_out = back_counter + chest_counter + legs_counter + abs_counter
konsumators = protein_shake_counter + protein_bar_counter

protzent_work_out = work_out / visitors * 100
protzent_konsumator = konsumators / visitors * 100

print(f'{back_counter} - back')
print(f'{chest_counter} - chest')
print(f'{legs_counter} - legs')
print(f'{abs_counter} - abs')
print(f'{protein_shake_counter} - protein shake')
print(f'{protein_bar_counter} - protein bar')
print(f'{protzent_work_out:.2f}% - work out')
print(f'{protzent_konsumator:.2f}% - protein')