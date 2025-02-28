# A year is a leap year if:
# It is divisible by 400 (e.g., 2000, 2400).
# It is divisible by 4 but not by 100 (e.g., 2024, 2028).

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

year = int(input())
print(is_leap(year))