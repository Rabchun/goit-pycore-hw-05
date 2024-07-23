import re

def generator_numbers(text: str) -> float:

    for match in re.finditer(r"\s+([0-9]*\.[0-9]+|[0-9]+)\s+", text):
        yield float(match.group(1))

def sum_profit(text: str, func=generator_numbers) -> float:
    
    total = 0
    for number in func(text):
        total += number
    return total