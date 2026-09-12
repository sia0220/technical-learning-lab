# Ask for a number of minutes.
minutes = int(input("Number of minutes: "))

# Convert it into hours and remaining minutes.
hours = minutes // 60
minutes_left = minutes - hours * 60

print(f"This is {hours} hours and {minutes_left} minutes.")

