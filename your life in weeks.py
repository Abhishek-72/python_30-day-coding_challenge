age = input("what is your current age? ")
age_as_int = int(age)

years_remaining = 90 - age_as_int  # i have supposed to live maximum 90 year
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"you have {days_remaining} days, {weeks_remaining}, weeks,{months_remaining} months"
print(message)