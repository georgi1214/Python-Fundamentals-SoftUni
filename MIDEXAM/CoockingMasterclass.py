from math import ceil


def aprons(students):
    apronas = ceil(students * 1.20)
    return apronas


def flour(students):
    flours = 0
    for i in range(1, students + 1):
        flours += 1
        if i % 5 == 0:
            flours -= 1
    return flours


budget = float(input())
students = int(input())
flour_price = float(input())
price_per_egg = float(input())
price_per_apron = float(input())

budget_needed = price_per_apron * aprons(students) + students * 10 * price_per_egg + flour(students) * flour_price

if budget_needed <= budget:
    print(f"Items purchased for {budget_needed:.2f}$.")
else:
    print(f"{abs(budget_needed - budget):.2f}$ more needed.")