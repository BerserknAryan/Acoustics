import math
import scipy.optimize
import json
from optimize import optimize_dimensions
from Isobaric import Isobaric
from Horns import Horns
from Constants import c

# Function to get driver configuration
def get_driver_config(driver_name):
    try:
        with open('driver_configs.json', 'r') as file:
            driver_configs = json.load(file)
        return driver_configs.get(driver_name)
    except FileNotFoundError:
        return None

# Function to save driver configuration
def save_driver_config(driver_name, driver_config):
    try:
        with open('driver_configs.json', 'r') as file:
            driver_configs = json.load(file)
    except FileNotFoundError:
        driver_configs = {}
    driver_configs[driver_name] = driver_config
    with open('driver_configs.json', 'w') as file:
        json.dump(driver_configs, file)

# Main functionality
try:
    driver_name = input("Enter driver name (e.g., Tropo18d4_1, Tropo18d4_2): ")
    driver_config = get_driver_config(driver_name)

    if driver_config:
        print(f"Using saved configuration for {driver_name}.")
    else:
        print(f"No saved configuration found for {driver_name}. Please enter driver parameters.")
        fs = float(input("Enter fs: "))
        qts = float(input("Enter qts: "))
        vas_liters = float(input("Enter vas in liters: "))
        sd = float(input("Enter sd (cm^2): "))
        desired_width = float(input("Enter desired width: "))
        driver_config = {'fs': fs, 'qts': qts, 'vas_liters': vas_liters, 'sd': sd, 'desired_width': desired_width}
        save_driver_config(driver_name, driver_config)

        # Additional inputs for the horn design
        desired_T = float(input("Enter desired T (0.1-10): "))
        desired_fg = float(input("Enter desired frequency at -3dB start (Hz): "))
        drivers = int(input("Enter number of drivers: "))

        # Convert vas from liters to cubic decimeters (dm^3)
        vas_dm3 = vas * 1000
        location_of_horn = int(input("Enter location of horn: "))
        amt = (c * c / (4 * math.pi * desired_fg * desired_fg)) / location_of_horn
        fg = math.sqrt(c * c / (4 * math.pi * amt))

        # Calculate required back chamber
        back_chamber = vb
        if drivers == 1:
            vb = vas_dm3 / ((fg / (fs * qts)) - 1)
        else:
            effective_vas = vas_dm3 * drivers
            vb = (effective_vas * fs * qts) / fg

        print("Calculating horn dimensions..."),
        print("Error: Please enter valid numerical values.")

        def calculate_horn_dimensions_and_response(t, driver_name):
            # Calculate throat area
            at = (2 * 3.1416 * fs * qts * vas_dm3) / c

            # Calculate mouth area
            amt = at * t

            # Calculate cross-sectional area
            ax = math.sqrt(at * amt)

            # Check if throat area is zero
            if at == 0:
                return None, None, None, None, None, None, None, None, None, None, None, "Error: Throat area is zero. Desired T value is not achievable with the given parameters."

            # Check if mouth area is greater than throat area
            if amt <= at:
                return None, None, None, None, None, None, None, None, None, None, None, "Error: Desired T value is not achievable with the given parameters."

            # Calculate horn length
            L = (amt * (t ** 2)) / (2 * 3.1416 * math.sqrt(amt / at - 1))

            # Convert at and amt to square inches
            at_in2 = at * 1550.0031
            amt_in2 = amt * 1550.0031

            # Convert horn length to feet
            L_ft = L * 3.28084

            # Calculate width and height for at and amt
            width_at = math.sqrt(at_in2)
            height_at = width_at
            width_amt = math.sqrt(amt_in2)
            height_amt = width_amt

            # Calculate taper rate
            taper_rate = (math.sqrt(amt / at - 1)) / L

            # Calculate frequency range response
            Fl = driver_name / math.sqrt(2 * 3.1416 * at * L)
            Fh = driver_name / math.sqrt(2 * 3.1416 * amt * L)

            return at, amt, ax, L, taper_rate, at_in2, amt_in2, L_ft, width_at, height_at, width_amt, height_amt, Fl, Fh


        # Define objective function
        def objective(T, fs, qts, vas_dm3, driver, desired_width):
            _, _, _, _, _, _, _, _, _, width_amt, _, _, _ = calculate_horn_dimensions_and_response(fs, qts, vas_dm3, T,
                                                                                                   driver)
            return abs(width_amt - desired_width)


        # Initial guess for T
        T0 = 1

        # Use scipy.optimize.minimize to find optimal T
        result = scipy.optimize.minimize(objective, T0, args=(fs, qts, vas_dm3, driver_name, desired_width))

        # Check if the optimizer has found a solution
        if result.success:
            optimal_t = result.x[0]
        else:
            print("Error: The optimization process did not converge.")
            exit()

        # Calculate horn dimensions with optimal T
        (at, amt, ax, L, taper_rate, at_in2, amt_in2, L_ft, width_at, height_at, width_amt,
         height_amt, Fl, Fh) = optimize_dimensions(fs, qts, vas_dm3, optimal_t, driver_)

        # Calculate horn dimensions
        at_in_sq, amt_in_sq, L_in, taper_rate = optimize_dimensions(fs, qts, vas_dm3, desired_T)

        # Print horn dimensions in imperial units with labels
        print("Throat Area (at) in square inches: ", at_in_sq)
        print("Mouth Area (amt) in square inches: ", amt_in_sq)
        print("Horn Length (L) in inches: ", L_in)
        print("Taper Rate: ", taper_rate)

        # Print cutsheet
        print("Cutsheet for building the enclosure:")
        print("Throat Area (at): ", at_in_sq, " square inches")
        print("Mouth Area (amt): ", amt_in_sq, " square inches")
        print("Horn Length (L): ", L_in, " inches")
        print("Taper Rate: ", taper_rate)

        print("Where is this horn going?")
        print("0 free space, 2 on floor, 4 on floor against wall, 8 in a corner")

        print("the horn is of infinite length and the wavelength 'fits' "
              "the horn then the mouth area Am must comply to formula:")
        print(amt)

        print("When the mouth area Am of two horns are placed beside each other, then the result will")
        print("be better performance in the lowest bass because the area is now doubled.")
        print("The next formula can be used to see if we can lower the frequency fg by the enlargement")
        print("of Am.")

        print("Mind in the calculation where you want to place the horn, by placement in the corner")
        print("the surface amt must be multiplied by 8!")

        print(fg)

        print("Back chamber:")

        # Adjust vb based on conditions
        if vb > vas_dm3:
            vb = (vas_dm3 * fs * qts) / fg
        elif vas_dm3 < vb:
            vb = vas_dm3 / ((fg / (fs * qts)) - 1)

        print("Back chamber:")
        
        compression_chamber = input("Do you have a compression chamber? (yes/no): ")

        if compression_chamber.lower() == "yes":
            Vf_liters = float(input("Enter volume of compression chamber in liters: "))
            # Convert Vf from liters to cubic decimeters (dm^3)
            Vf_dm3 = Vf_liters * 1000
            crossover = 2 * qts * fs * (effective_vas / Vf_dm3)
            print("-3dB crossover point is", crossover)
        else:
            print("Pass")

    else:
        print("Driver configuration not found.")