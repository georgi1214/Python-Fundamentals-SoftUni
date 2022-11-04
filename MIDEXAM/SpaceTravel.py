courses = list(x for x in input().split("||"))
initial_fuel = int(input())
ammo = int(input())

fuel_left = initial_fuel
ammo_left = ammo
for action in courses:
    current_action = action.split(" ")
    if current_action[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    if len(current_action) > 1:
        command = current_action[0]
        info = int(current_action[1])
    if current_action[0] == "Travel":
        if fuel_left >= info:
            print(f"The spaceship travelled {info} light-years.")
            fuel_left -= info
        else:
            print("Mission failed.")
            break
    if current_action[0] == "Enemy":
        if ammo_left >= info:
            ammo_left -= info
            print(f"An enemy with {info} armour is defeated.")
        elif ammo_left < info:
            if fuel_left >= (info * 2):
                fuel_left -= (info * 2)
                print(f"An enemy with {info} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    if current_action[0] == "Repair":
        fuel_left += info
        ammo_left += (info * 2)
        print(f"Ammunitions added: {info * 2}.")
        print(f"Fuel added: {info}.")