def odd_even_sum(number: int):
    """function that returns the sum of all even and all odd digits in a given number.
    The result should be returned as a single string in the format: """
    even_sum = 0
    odd_sum = 0
    num_to_str = str(number)
    for element in num_to_str:
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


digit = int(input())
print(odd_even_sum(digit))