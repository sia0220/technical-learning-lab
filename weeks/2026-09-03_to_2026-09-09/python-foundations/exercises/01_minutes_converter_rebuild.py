# Ask for a number of minutes.
minutes = int(input("Number of minutes: "))

# Convert into remaining hours and minutes.
remaining_hours = minutes // 60
remaining_minutes = minutes - remaining_hours * 60 

# Display clear results.
print(f"The remaining time is {remaining_hours} hours and {remaining_minutes} minutes.")