days_adv = int(input())
player_count = int(input())
group_energy = float(input())
water_per_day_per_player = float(input())
food_per_day_per_player = float(input())

total_water = days_adv * water_per_day_per_player * player_count
total_food = days_adv * food_per_day_per_player * player_count

for current_day in range(1, days_adv + 1):
    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    if current_day % 2 == 0:
        group_energy += group_energy * 0.05
        total_water -= total_water * 0.30
    if current_day % 3 == 0:
        total_food -= (total_food / player_count)
        group_energy += group_energy * 0.10
if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")