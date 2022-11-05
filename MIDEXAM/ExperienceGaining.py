needed_experience = float(input())
count_of_battles = int(input())

result_of_experience = 0
counter_of_battles = 0


for i in range(count_of_battles):
    experience_per_battle = float(input())
    counter_of_battles += 1
    result_of_experience += experience_per_battle
    if counter_of_battles == 3:
        result_of_experience = experience_per_battle + (experience_per_battle * 0.15)
    if counter_of_battles == 5:
        result_of_experience = experience_per_battle - (experience_per_battle * 0.10)
    if counter_of_battles == 15:
        result_of_experience = experience_per_battle + (experience_per_battle + 0.05)
    if result_of_experience >= needed_experience:
        break
if result_of_experience >= needed_experience:
    print(f'Player successfully collected his needed experience for {counter_of_battles} battles.')
else:
    print(f'Player was not able to collect the needed experience, {result_of_experience} more needed.')

