import math
import scipy.optimize


# Function to get horn shape based on flair rate t
def get_horn_shape(t):
    if 0 <= t <= 2:
        return "conical"
    elif 2.1 <= t <= 4:
        return "tractrix"
    elif 3 <= t <= 5:
        return "exponential"
    elif 4 <= t <= 6:
        return "parabolic"
    elif 5.1 <= t <= 8:
        return "elliptical"
    elif 6 <= t <= 7:
        return "hyperbolic"
    elif 8.1 <= t <= 10:
        return "hypersonic"
    else:
        return "Invalid t value"


# Function to calculate objective function
def objective_function(x, sd, fs, low_freq, high_freq, fc, t):
    t, throat_area, mouth_area, ax, horn_length = x
    objective = (abs(t - (mouth_area / throat_area)) + abs
                    (ax - math.sqrt(max(0, mouth_area / math.pi))))
    objective += abs(sd - throat_area * (math.sqrt(2 * math.pi) * math.sqrt(fs)))
    throat_freq = fs * math.sqrt(throat_area / sd)
    objective += max(0, low_freq - throat_freq) ** 2 + max(0, throat_freq - high_freq) ** 2
    return objective


# Function to find optimal values using optimization method from SciPy
def find_optimal_values(sd, fs, low_freq, high_freq, fc, t):
    x0 = [1, 1, 1, 1, 1]  # Initial guess for t, throat_area, mouth_area, ax, horn_length
    fh = high_freq
    fl = low_freq


    def f(x):
        return fl + (fh - fl) * x[0]

    constraints = [{'type': 'ineq', 'fun': lambda x: x[0]},  # t > 0
                   {'type': 'ineq', 'fun': lambda x: 10 - x[0]},  # t < 10
                   {'type': 'ineq', 'fun': lambda x: x[1] - sd},  # throat_area > 0+
                   {'type': 'ineq', 'fun': lambda x: x[2] - math.pi},  # mouth_area > pi
                   {'type': 'ineq', 'fun': lambda x: x[2]},  # mouth_area > 0
                   {'type': 'ineq', 'fun': lambda x: x[3]},  # ax > 0
                   {'type': 'ineq', 'fun': lambda x: x[4]},  # horn_length > 0
                   {'type': 'eq', 'fun': lambda x: x[2]},  # desired horn frequency cutoff
                   {'type': 'ineq', 'fun': lambda x: x[2] - math.pi},  # mouth_area >= pi
                   {'type': 'ineq', 'fun': lambda x: x[2] - x[1]},  # mouth_area >= throat_area
                   {'type': 'ineq', 'fun': lambda x: fh - f(x)},  # f(x) <= fh
                   {'type': 'ineq', 'fun': lambda x: f(x) - fl}]  # f(x) >= fl

    result = scipy.optimize.minimize(
        objective_function, x0, args=(sd, fs, low_freq, high_freq, fc, t),
        constraints=constraints, options={'disp': True}
    )

    return result.x

# Inputs
try:
    max_length = float(input("Enter the maximum length of enclosure (in inches): "))
    max_width = float(input("Enter the maximum width of enclosure (in inches): "))
    max_depth = float(input("Enter the maximum depth of enclosure (in inches): "))
    fs = float(input("Enter the driver's resonant frequency (fs): "))
    Qts = float(input("Enter the driver's total Q (Qts): "))
    Vas = float(input("Enter the driver's Vas (in cubic feet): "))
    sd = float(input("Enter the driver's sd (in square inches): "))
    xmax = float(input("Enter the driver's xmax: "))
    fc = float(input("Enter the desired horn frequency cutoff: "))

    # Calculate low and high frequencies
    low_freq = (fs * Qts) / 2
    high_freq = (2 * fs) / Qts

    # Get the flair rate t
    t = float(input("Enter desired T (0.1-10): "))

    if not (0.1 <= t <= 10):
        raise ValueError("T value must be between 0.1 and 10")

    selected_shape = get_horn_shape(t)
    print(f"The selected horn shape for t={t} is {selected_shape}.")

    # Find optimal values
    (optimal_t, optimal_throat_area, optimal_mouth_area, optimal_ax,
     optimal_horn_length) = find_optimal_values(sd, fs, low_freq, high_freq, fc, t)

    # Output
    print("Optimal flair rate:", optimal_t)
    print("Optimal throat area:", optimal_throat_area)
    print("Optimal mouth area:", optimal_mouth_area)
    print("Optimal ax:", optimal_ax)
    print("Optimal horn length:", optimal_horn_length)

except ValueError as e:
    print("Invalid input:", e)
