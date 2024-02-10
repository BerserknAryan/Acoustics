import math
import os
from Isobaric import Isobaric
from optimize import optimize_dimensions


# Function to save state to file
def save_state(filename, state):
    with open(filename, 'w') as file:
        for key, value in state.items():
            file.write(f"{key}:{value}\n")


# Function to load state from file
def load_state(filename):
    state = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(':')
                state[key] = eval(value)
    return state


# Check if state file exists
state_file = 'state.txt'
state = load_state(state_file)


# Function to calculate horn path dimensions
def calculate_horn_dimensions_and_response(fs, qts, vas_dm3, desired_t, driver):
    # Calculate throat area
    ah = (2 * 3.1416 * fs * qts * vas_dm3) / 343

    # Calculate mouth area
    amt = ah * desired_t

    # Check if throat area is zero
    if ah == 0:
        return (None, None, None, None, None, None, None, None, None, None, None,
                "Error: throat area is zero. Desired t value is not achievable with the given parameters.")

    # Check if mouth area is greater than throat area
    if amt <= ah:
        return (None, None, None, None, None, None, None, None, None, None, None,
                "Error: Desired t value is not achievable with the given parameters.")

    # Calculate horn length
    L = (amt * (desired_t ** 2)) / (2 * 3.1416 * math.sqrt(amt / ah - 1))

    # Convert ah and amt to square inches
    ah_in2 = ah * 1550.0031
    amt_in2 = amt * 1550.0031

    # Convert horn length to feet
    l_ft = L * 3.28084

    # Calculate width and height for ah and amt
    width_ah = math.sqrt(ah_in2)
    height_ah = width_ah
    width_amt = math.sqrt(amt_in2)
    height_amt = width_amt

    # Calculate taper rate
    taper_rate = (math.sqrt(amt / ah - 1)) / L

    # Calculate frequency range response
    fl = driver / math.sqrt(2 * 3.1416 * ah * L)
    fh = driver / math.sqrt(2 * 3.1416 * amt * L)

    return ah, amt, L, taper_rate, ah_in2, amt_in2, l_ft, width_ah, height_ah, width_amt, height_amt, fl, fh


# Function to print horn dimensions
def print_horn_dimensions(taper_rate, ah_in2, amt_in2, l_ft, width_ah, height_ah, width_amt, height_amt):
    print("throat Area (ah) in square inches: ", ah_in2)
    print("Mouth Area (amt) in square inches: ", amt_in2)
    print("Horn Length (L) in feet: ", l_ft)
    print("taper Rate: ", taper_rate)
    print("ah (width x height): {:.2f} in x {:.2f} in".format(width_ah, height_ah))
    print("amt (width x height): {:.2f} in x {:.2f} in".format(width_amt, height_amt))


# Continue script from last known point or start from the beginning
if not state or input("Do you want to start fresh or from the last known point? (fresh/last): ").lower() == 'fresh':
    fs = float(input("Enter fs: "))
    qts = float(input("Enter qts: "))
    vas_liters = float(input("Enter vas in liters: "))

    print("Options:")
    print("1: 1 driver, 1 horn")
    print("2: 2 drivers, 1 horn")
    print("3: isobaric, 1 horn")
    print("4: 2 drivers, 2 horns")
    option = int(input("Enter your choice (1-4): "))

    # Handling different configuration options
    if option == 1:
        drivers = 1
        horns = 1
    elif option == 2:
        drivers = 2
        horns = 1
    elif option == 3:
        drivers = Isobaric
        horns = 1
        # Calculate the enclosure volume for vented isobaric conditions
        enclosure_volume = Isobaric.isobaric(vas_liters, qts)
        # Calculate the tuning frequency for vented enclosure in isobaric conditions
        tuning_frequency = Isobaric.vented_isobaric_tuning_frequency(vas_liters, qts, enclosure_volume)
        # Calculate optimal port area for vented enclosure in isobaric conditions
        port_area = Isobaric.vented_isobaric_port_area(tuning_frequency, enclosure_volume)
        # Calculate required port length for vented enclosure in isobaric conditions
        port_length = Isobaric.vented_isobaric_port_length(port_area, tuning_frequency)
        # Estimate air speed within the port for vented enclosure in isobaric conditions
        air_speed = Isobaric.vented_isobaric_air_speed(port_area, tuning_frequency, enclosure_volume)
    elif option == 4:
        drivers = 2
        horns = 2
    else:
        print("Invalid option selected. Exiting script.")
        exit()

    # Convert vas from liters to cubic decimeters (dm^3)
    vas_dm3 = vas_liters * 1000
    desired_t = float(input("Enter desired t (0.1-10): "))
    desired_Fg = float(input("Enter desired frequency at -3dB start (Hz): "))  # Added this line
    Sd = float(input("Enter Sd (cm^2): "))
    desired_width = float(input("Enter desired width: "))
    (optimal_t, ah, amt, L, taper_rate, ah_in2, amt_in2, l_ft, width_ah, height_ah, width_amt, height_amt, fl,
     fh) = optimize_dimensions(
        fs, qts, vas_dm3, desired_Fg, Sd, desired_width)

    print("Calculating horn dimensions...")

    # Calculate horn dimensions
    (ah, amt, L, taper_rate, ah_in2, amt_in2, l_ft, width_ah, height_ah, width_amt,
     height_amt, fl, fh) = calculate_horn_dimensions_and_response(fs, qts, vas_dm3, desired_t, desired_Fg)
    # Updated this line

    if ah is not None:
        # Print horn dimensions
        print_horn_dimensions(taper_rate, ah_in2, amt_in2, l_ft, width_ah, height_ah, width_amt, height_amt)

        # Save state
        state = {
            'ah': ah,
            'amt': amt,
            'L': L,
            'taper_rate': taper_rate,
            'ah_in2': ah_in2,
            'desired_t': desired_t,
            'desired_Fg': desired_Fg,
            'desired_width': desired_width,
            'Sd': Sd,
            'fs': fs,
            'qts': qts,
            'vas_dm3': vas_dm3,
            'amt_in2': amt_in2,
            'l_ft': l_ft,
            'width_ah': width_ah,
            'height_ah': height_ah,
            'width_amt': width_amt,
            'height_amt': height_amt,
            'fl': fl,
            'fh': fh
        }
        save_state(state_file, state)
        if 'ah_in2' in state:
            print("Continuing from last known point.")
        print_horn_dimensions(state['taper_rate'], state['ah_in2'], state['amt_in2'], state['l_ft'], state['width_ah'],
                              state['height_ah'], state['width_amt'], state['height_amt']),
        print("Error: State file does not contain necessary data. Starting fresh.")
        
    else:
        print("Error occurred. Horn dimensions could not be calculated with the given parameters.")

else:
    print("Continuing from last known point.")
