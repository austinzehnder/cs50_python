# Get mass from the user as an integer (in kilograms)
mass_kg = int(input("Mass (in kilograms): "))

# Speed of light in meters per second
speed_of_light = 300000000

# Calculate energy using E=mc^2
energy_joules = mass_kg * speed_of_light ** 2

# Output the equivalent energy in Joules
print("E:", energy_joules,)
