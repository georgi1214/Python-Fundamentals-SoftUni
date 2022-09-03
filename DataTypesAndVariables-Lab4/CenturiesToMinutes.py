num = int(input())

centuries = num * 100
years = int(centuries * 365.2422)
days = years * 24
hours = int(days * 60)

print(f'{num} centuries = {centuries} years = {years} days = {days} hours = {hours} minutes')