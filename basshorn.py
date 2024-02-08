import math


# Function to calculate horn path dimensions
def calculate_horn_dimensions(Fs, Qts, Vas_dm3, desired_T):
    # Convert throat and mouth dimensions from inches to square inches
    Ah_in_sq = (2 * math.pi * Fs * Qts * Vas_dm3) / 343
    Amt_in_sq = Ah_in_sq * desired_T

    # Convert horn length from meters to inches
    L_in = (Amt_in_sq * (desired_T**2)) / (2 * math.pi * math.sqrt(Amt_in_sq / Ah_in_sq - 1)) * 39.3701

    # Calculate taper rate (no need to convert)
    taper_rate = (math.sqrt(Amt_in_sq / Ah_in_sq - 1)) / L_in

    return Ah_in_sq, Amt_in_sq, L_in, taper_rate


def get_driver_config(driver_name):
    driver_configs = {
        "Tropo18d4_1": {"Fs": 23.6, "Qts": 0.754, "Vas_liters": 6.83},
        "Tropo18d4_2": {"Fs": 23.4, "Qts": 0.31, "Vas_liters": 6.83},
        # Add more driver configurations as needed
    }
    return driver_configs.get(driver_name)


try:
    driver_name = input("Enter driver name (e.g., Tropo18d4_1, Tropo18d4_2): ")
    driver_config = get_driver_config(driver_name)

    if driver_config:
        Fs = driver_config["Fs"]
        Qts = driver_config["Qts"]
        Vas_liters = driver_config["Vas_liters"]

        # Additional inputs for the horn design
        desired_T = float(input("Enter desired T (0.1-10): "))
        desired_Fg = float(input("Enter desired frequency at -3dB start (Hz): "))
        drivers = int(input("Enter number of drivers: "))

        # Convert Vas from liters to cubic decimeters (dm^3)
        Vas_dm3 = Vas_liters * 1000
        location_of_horn = int(input("Enter location of horn: "))
        Amt = (343 * 343 / (4 * math.pi * desired_Fg * desired_Fg)) / location_of_horn
        Fg = math.sqrt(343 * 343 / (4 * math.pi * Amt))

        # Separate routes for single drivers and multiple drivers in one enclosure
        if drivers == 1:
            Vb = Vas_dm3 / ((Fg / (Fs * Qts)) - 1)
        else:
            effective_Vas = Vas_dm3 * drivers
            Vb = (effective_Vas * Fs * Qts) / Fg

        print("Calculating horn dimensions...")

        # Calculate horn dimensions
        Ah_in_sq, Amt_in_sq, L_in, taper_rate = calculate_horn_dimensions(Fs, Qts, Vas_dm3, desired_T)

        # Print horn dimensions in imperial units with labels
        print("Throat Area (Ah) in square inches: ", Ah_in_sq)
        print("Mouth Area (Amt) in square inches: ", Amt_in_sq)
        print("Horn Length (L) in inches: ", L_in)
        print("Taper Rate: ", taper_rate)

        # Print cutsheet
        print("Cutsheet for building the enclosure:")
        print("Throat Area (Ah): ", Ah_in_sq, " square inches")
        print("Mouth Area (Amt): ", Amt_in_sq, " square inches")
        print("Horn Length (L): ", L_in, " inches")
        print("Taper Rate: ", taper_rate)

        print("Where is this horn going?")
        print("0 free space, 2 on floor, 4 on floor against wall, 8 in a corner")

        print("the horn is of infinite length and the wavelength 'fits' "
              "the horn then the mouth area Am must comply to formula:")
        print(Amt)

        print("When the mouth area Am of two horns are placed beside each other, then the result will")
        print("be better performance in the lowest bass because the area is now doubled.")
        print("The next formula can be used to see if we can lower the frequency Fg by the enlargement")
        print("of Am.")

        print("Mind in the calculation where you want to place the horn, by placement in the corner")
        print("the surface Amt must be multiplied by 8!")

        print(Fg)

        print("Back chamber:")

        # Adjust Vb based on conditions
        if Vb > Vas_dm3:
            Vb = (Vas_dm3 * Fs * Qts) / Fg
        elif Vas_dm3 < Vb:
            Vb = Vas_dm3 / ((Fg / (Fs * Qts)) - 1)

        compression_chamber = input("Do you have a compression chamber? (yes/no): ")

        if compression_chamber.lower() == "yes":
            Vf_liters = float(input("Enter volume of compression chamber in liters: "))
            # Convert Vf from liters to cubic decimeters (dm^3)
            Vf_dm3 = Vf_liters * 1000
            crossover = 2 * Qts * Fs * (effective_Vas / Vf_dm3)
            print("-3dB crossover point is", crossover)
        else:
            print("Pass")

    else:
        print("Driver configuration not found.")

except ValueError:
    print("Error: Please enter valid numerical values.")
