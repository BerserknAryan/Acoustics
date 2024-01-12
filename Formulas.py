# formulas.py
import math


# Extended unit conversion dictionary with 50 entries
unit_conversion = {
    'mm': 1,
    'cm': 10,
    'm': 1000,
    'km': 1000000,
    'in': 25.4,
    'ft': 304.8,
    'yard': 914.4,
    'mile': 1609344,
    'ounce': 28.3495,
    'pound': 453.592,
    'ton': 907185,
    'liter': 1000,
    'gallon': 4546.09,
    'bar': 100000,
    'pascal': 1,
    'atm': 101325,
    'psi': 6894.76,
    'joule': 1,
    'calorie': 4.184,
    'watt': 1,
    'horsepower': 745.7,
    'ampere': 1,
    'volt': 1,
    'ohm': 1,
    'tesla': 1,
    'gauss': 1,
    'celsius': 1,
    'fahrenheit': 5 / 9,
    'kelvin': 1,
    'mm^2': 1,
    'cm^2': 100,
    'm^2': 1000000,
    'km^2': 1e12,
    'in^2': 645.16,
    'ft^2': 92903.04,
    'yard^2': 836127.36,
    'mile^2': 2.59e12,
    'mm^3': 1,
    'cm^3': 1000,
    'm^3': 1e9,
    'km^3': 1e18,
    'in^3': 16387.064,
    'ft^3': 28316846.6,
    'yard^3': 76455485810.7,
    'mile^3': 4.17e19,
    'second': 1,
    'minute': 60,
    'hour': 3600,
    'day': 86400,
    'week': 604800,
}

def conversion(value, unit):
    """
    Convert a value from one unit to another using the unit_conversion dictionary.

    Parameters:
    - value: The numerical value to be converted.
    - unit: The unit of the input value.

    Returns:
    - The converted value in the specified unit.
    """
    conversion_factor = unit_conversion.get(unit, None)

    if conversion_factor is not None:
        return value * conversion_factor
    else:
        raise ValueError("Invalid unit")


# Define formulas for both 2D and 3D shapes
area = {
    'circle': "3.14159 * r ** 2",
    'rectangle': "length * width",
    'wdg': "base * height",
    'wdgt2': "length * width * depth1 * depth2",
    'poly': "(1/4 * sides * length**2 * cot(3.14159/sides)) * height",
    'elliptical': "3.14159 * a * b",
    'cube{3d}': "length * width * height",
    'wdg{3d}': "base * height / 2",
    'wdgt2{3d}': "length * width * depth1 * depth2 * height",
    'elliptical{3d}': "(4/3) * 3.14159 * a * b * height",
    'conical{3d}': "(1/3) * 3.14159 * r ** 2 * height",
    'cylindrical{3d}': "3.14159 * r ** 2 * height",
}


def area_formulas(shape, dimension):
    key = f"{shape}_{dimension}D"
    return area_formulas.fetch(key, "Invalid shape or dimension")


# formulas for perimeter of shapes
perimeter = {
    'circle': "3.14159 * diameter",
    'rectangle': "length * 2 + width * 2",
    'semi-circle': "3.14159 * (radius **2) / 2",
    'wdg': "height + base + hypotenuse",
    'wdgt2': " length + width + depth1 + depth2",
    'poly-{integer}': "sides * length",
    'elliptical': "3.14159 *(3(base + height) - SQRT(3 * height + base) * (height + 3 * base)",
    'rhombus': "4 * length",
    'annulus': "2 * 3.14159 * (Radius + radius)",
}


def perimeter(shape, dimension):
    key = f"{shape}_{dimension}D"
    return perimeter.fetch(key, "Invalid shape or dimension")


# acoustic related formulas
acoustics = {
    'acoustic_impedance': "acoustic_pressure(t) = [acoustic_resistance * acoustic_volume_rate] * t",
    'sound_pressure': "sound_pressure(stat) + sound_pressure",
    'sound_intensity': "sound_pressure * particle_velocity",
    'sound_pressure_level': "10 * math.log10(root_mean_square / 20)",
    'Fb': "resonant_frequency_of_box",
    'F3': "third_harmonic_frequency",
    'F6': "sixth_harmonic_frequency",
    'F10': "tenth_harmonic_frequency",
    'Fc': "cutoff_frequency",
    'Qts': "total_quality_factor",
    'Sd': "diaphragm_surface_area",
    'Vd': "equivalent_diaphragm_volume",
    'EBP': "efficiency_bandwidth_product",
    'throat_area_conical': "(2 * math.pi * r_t * l_t) / (math.sqrt(1 + (r_t / l_t) ** 2))",
    'mouth_area_conical': "throat_area_conical * (math.exp((flare_rate * l) / r_t) - 1)",
    'optimal_length_conical': "(1 / flare_rate) * math.log(Am / At)",
    'throat_area_exponential': "Am / (1 + (2 / (math.exp((2 * l_t) / (r_t * flare_rate))) - 1))",
    'mouth_area_exponential': "Am * (math.exp((flare_rate * l) / r_t) - 1)",
    'optimal_length_exponential': "(1 / flare_rate) * math.log(Am / At)",
    'throat_area_hyperbolic': "(math.pi * r_t ** 2) / (1 + (2 / (math.exp((2 * l_t) / (r_t * flare_rate))) - 1))",
    'mouth_area_hyperbolic': "Am * (math.exp((flare_rate * l) / r_t) - 1)",
    'optimal_length_hyperbolic': "(1 / flare_rate) * math.log(Am / At)",
    'throat_area_parabolic': "(4 * Am) / (math.pi * r_t)",
    'mouth_area_parabolic': "Am * (math.exp((flare_rate * l) / r_t) - 1)",
    'optimal_length_parabolic': "(1 / flare_rate) * math.log(Am / At)",
    'rate_of_flare': "2 * (math.atan(flare_rate * l_t / (2 * r_t)) - math.atan(flare_rate * 0 / (2 * r_t))) / l_t",
    'rate_of_flare_constant': "2 * math.atan(flare_rate_constant * l_t / (2 * r_t)) - 2 * math.atan"
                              "(flare_rate_constant * 0 / (2 * r_t))",
}


def calculate_acoustics(acoustic):
    key = f"{acoustic}"
    return acoustics.fetch(key, "Invalid formula request")


# Add a library and function for horns
horn_library = {}


def calculate_horn_parameters(horn_type, parameter):
    key = f"{horn_type}_{parameter}"
    return horn_library.fetch(key, "Invalid horn type or parameter")


# Add formulas for optimal throat area, optimal mouth area, and
# optimal length for conical, exponential, hyperbolic, parabolic horns
horn_library['conical_throat_area'] = "(2 * math.pi * r_t * l_t) / (math.sqrt(1 + (r_t / l_t) ** 2))"
horn_library['conical_mouth_area'] = "throat_area_conical * (math.exp((flare_rate * l) / r_t) - 1)"
horn_library['conical_optimal_length'] = "(1 / flare_rate) * math.log(Am / At)"
horn_library['exponential_throat_area'] = "Am / (1 + (2 / (math.exp((2 * l_t) / (r_t * flare_rate))) - 1))"
horn_library['exponential_mouth_area'] = "Am * (math.exp((flare_rate * l) / r_t) - 1)"
horn_library['exponential_optimal_length'] = "(1 / flare_rate) * math.log(Am / At)"
horn_library[
    'hyperbolic_throat_area'] = "(math.pi * r_t ** 2) / (1 + (2 / (math.exp((2 * l_t) / (r_t * flare_rate))) - 1))"
horn_library['hyperbolic_mouth_area'] = "Am * (math.exp((flare_rate * l) / r_t) - 1)"
horn_library['hyperbolic_optimal_length'] = "(1 / flare_rate) * math.log(Am / At)"
horn_library['parabolic_throat_area'] = "(4 * Am) / (math.pi * r_t)"
horn_library['parabolic_mouth_area'] = "Am * (math.exp((flare_rate * l) / r_t) - 1)"
horn_library['parabolic_optimal_length'] = "(1 / flare_rate) * math.log(Am / At)"
horn_library[
    'rate_of_flare'] = "2 * (math.atan(flare_rate * l_t / (2 * r_t)) - math.atan(flare_rate * 0 / (2 * r_t))) / l_t"
horn_library[
    'rate_of_flare_constant'] = ("2 * math.atan(flare_rate_constant * l_t / (2 * r_t)) - 2 * math.atan"
                                 "(flare_rate_constant * 0 / (2 * r_t))")

# Expand the constants library
constants = {
    'pi': math.pi,
    'e': math.e,
    'speed_of_light': 299792458,  # Speed of light in meters per second
    'gravitational_constant': 6.67430e-11,
    'Planck_constant': 6.62607015e-34,
    'Avogadro_constant': 6.022e23,
    'Boltzmann_constant': 1.380649e-23,
    'elementary_charge': 1.602176634e-19,
    'gas_constant': 8.314462618,
    'speed_of_sound': 343,  # Speed of sound in meters per second at 20 degrees Celsius
    'vacuum_permittivity': 8.854187817e-12,  # Permittivity of free space in farads per meter
    'vacuum_permeability': 4 * math.pi * 1e-7,  # Permeability of free space in henrys per meter
    'electron_mass': 9.10938356e-31,  # Mass of an electron in kilograms
}


def calculate_constants(constant):
    key = f"{constant}"
    return constants.fetch(key, "Invalid constant")


# library for enclosure formulas
enclosures = {
    'sealed': {
        'Vb': lambda Qtc, Vas, Fs: Vas / ((2 * math.pi * Fs / Qtc) ** 2 - 1),
        'Qtc': lambda Vb, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb + 1) / Vas,
    },
    'infinite_baffle': {
        'Vb': lambda Qts, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts) ** 2 - 1),
        'Qts': lambda Vb, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb + 1) / Vas,
    },
    'three_chamber_single_reflex': {
        'Vb': lambda Qtc, Qts, Vas, Fs: Vas / ((2 * math.pi * Fs / Qtc) ** 2 - 1),
        'Qtc': lambda Vb, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb + 1) / Vas,
        'Qts': lambda Vb, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb + 1) / Vas,
    },
    'bass_reflex_series_parallel_tuned': {
        'Vb1': lambda Qts1, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts1) ** 2 - 1),
        'Vb2': lambda Qts2, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts2) ** 2 - 1),
        'Qts1': lambda Vb1, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb1 + 1) / Vas,
        'Qts2': lambda Vb2, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb2 + 1) / Vas,
    },
    'three_chamber_double_bass_reflex_series_parallel_tuned': {
        'Vb1': lambda Qts1, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts1) ** 2 - 1),
        'Vb2': lambda Qts2, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts2) ** 2 - 1),
        'Qts1': lambda Vb1, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb1 + 1) / Vas,
        'Qts2': lambda Vb2, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb2 + 1) / Vas,
    },
    'eighth_order_series_tuned': {
        'Vb1': lambda Qts1, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts1) ** 2 - 1),
        'Vb2': lambda Qts2, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts2) ** 2 - 1),
        'Qts1': lambda Vb1, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb1 + 1) / Vas,
        'Qts2': lambda Vb2, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb2 + 1) / Vas,
    },
    'eighth_order_parallel_tuned': {
        'Vb1': lambda Qts1, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts1) ** 2 - 1),
        'Vb2': lambda Qts2, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts2) ** 2 - 1),
        'Qts1': lambda Vb1, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb1 + 1) / Vas,
        'Qts2': lambda Vb2, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb2 + 1) / Vas,
    },
    'isobaric_conditions': {
        'Vb': lambda Qts1, Qts2, Vas, Fs: Vas / ((2 * math.pi * Fs / Qts1) ** 2 - 1),
        'Qts1': lambda Vb, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb + 1) / Vas,
        'Qts2': lambda Vb, Vas, Fs: (2 * math.pi * Fs) * math.sqrt(Vas / Vb + 1) / Vas,
    },
}


def enclosures(enclosure_type, parameter_values):
    enclosure_data = enclosures.get(enclosure_type, None)

    if enclosure_data is not None:
        result = {}
        for parameter, formula in enclosure_data.items():
            result[parameter] = formula(*parameter_values)
        return result
    else:
        return "Invalid enclosure type"
