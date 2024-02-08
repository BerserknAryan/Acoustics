import math

# Function to calculate horn path dimensions
def calculate_horn_dimensions(Fs, Qts, Vas_dm3, desired_T):
    # Calculate throat area
    Ah = (2 * 3.1416 * Fs * Qts * Vas_dm3) / 343

    # Calculate mouth area
    Amt = Ah * desired_T

    # Check if throat area is zero
    if Ah == 0:
        print("Error: Throat area is zero. Desired T value is not achievable with the given parameters.")
        return None, None, None, None

    # Check if mouth area is greater than throat area
    if Amt <= Ah:
        print("Error: Desired T value is not achievable with the given parameters.")
        return None, None, None, None

    # Calculate horn length
    L = (Amt * (desired_T**2)) / (2 * 3.1416 * math.sqrt(Amt/Ah - 1))

    # Calculate taper rate
    taper_rate = (math.sqrt(Amt/Ah - 1)) / L

    return Ah, Amt, L, taper_rate

# Function to save state to file
def save_state(filename, state):
    with open(filename, 'w') as file:
        for key, value in state.items():
            file.write(f"{key}:{value}\n")

# Function to load state from file
def load_state(filename):
    state = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            state[key] = eval(value)
    return state

# Function to print horn dimensions
def print_horn_dimensions(Ah, Amt, L, taper_rate):
    print("Throat Area (Ah) in square meters: ", Ah)
    print("Mouth Area (Amt) in square meters: ", Amt)
    print("Horn Length (L) in meters: ", L)
    print("Taper Rate: ", taper_rate)

# Check if state file exists
state_file = 'state.txt'
try:
    state = load_state(state_file)
    print("Loaded previous state from file.")
    print_horn_dimensions(state['Ah'], state['Amt'], state['L'], state['taper_rate'])
except FileNotFoundError:
    print("No previous state found. Starting from the beginning.")
    state = {}

# Continue script from last known point or start from the beginning
if 'Ah' not in state:
    Fs = float(input("Enter Fs: "))
    Qts = float(input("Enter Qts: "))
    Vas_liters = float(input("Enter Vas in liters: "))
    drivers = float(input("Enter number of drivers: "))
    horns = float(input("Enter number of horns: "))
    desired_T = float(input("Enter desired T (0.1-10): "))
    desired_Fg = float(input("Enter desired frequency at -3dB start (Hz): "))

    # Convert Vas from liters to cubic decimeters (dm^3)
    Vas_dm3 = Vas_liters * 1000

    print("Calculating horn dimensions...")

    # Calculate horn dimensions
    Ah, Amt, L, taper_rate = calculate_horn_dimensions(Fs, Qts, Vas_dm3, desired_T)

    if Ah is not None:
        # Print horn dimensions
        print_horn_dimensions(Ah, Amt, L, taper_rate)

        # Save state
        state['Ah'] = Ah
        state['Amt'] = Amt
        state['L'] = L
        state['taper_rate'] = taper_rate
        save_state(state_file, state)

    else:
        print("Error occurred. Exiting script.")
else:
    print("Continuing from last known point.")
