# formulas.py
import math
import numpy as np


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


constants = {'Pi': math.pi,
             'c': 343,  # Speed of sound in meters per second
             'epsilon_0': 8.854e-12,  # Vacuum permittivity in farads per meter
             'mu_0': 4e-7 * math.pi,  # Vacuum permeability in henry per meter
             'sigma': 5.67e-8,  # Stefan-Boltzmann constant in watts per square meter per kelvin^4
             'R': 8.314,  # Universal gas constant in joules per mole-kelvin
             'G': 6.67430e-11,  # Gravitational constant in m^3 kg^-1 s^-2
             'h': 6.626e-34,  # Planck constant in joule-seconds
             'k': 1.38e-23,  # Boltzmann constant in joules per kelvin
             'e': 1.602e-19,  # Elementary charge in coulombs
             'N_A': 6.022e23,  # Avogadro's number in mol^-1
             'k_e': 8.988e9,  # Coulomb's constant in newton-square meters per square coulomb^2
             'h_bar': 1.054e-34,  # Reduced Planck constant in joule-seconds
             'R_inf': 1.097e7,  # Rydberg constant in per meter
             'c_0': 299792458,  # Speed of light in vacuum in meters per second
             }


class FreeAir:
    @staticmethod
    def rear_deck_resonant_frequency(total_cms, effective_piston_area, fs):
        # Formula to calculate the resonant frequency for a speaker in the rear deck
        return (1 / (2 * 3.141592) * math.sqrt
                ((total_cms / effective_piston_area) + fs ** 2))

    @staticmethod
    def rear_seat_resonant_frequency(total_cms, effective_piston_area, fs):
        # Formula to calculate the resonant frequency for a speaker in the rear seat
        return (1 / (2 * 3.141592) * math.sqrt
                ((total_cms / effective_piston_area) + fs ** 2))

    @staticmethod
    def small_deck_resonant_frequency(total_cms, effective_piston_area, small_deck_volume, fs):
        # Formula to calculate the resonant frequency for a speaker mounted in or out of a small deck
        return (1 / (2 * 3.141592) * math.sqrt
                (((total_cms + (small_deck_volume * 1000)) /
                    effective_piston_area) + fs ** 2))

    @staticmethod
    def floorboard_resonant_frequency(total_cms, effective_piston_area, cone_area, fs):
        # Formula to calculate the resonant frequency for a speaker installed in the
        # floorboard at the feet firing cone at you
        return 1 / (2 * 3.141592) * math.sqrt(((total_cms + (cone_area * 1000)) / 
                                               effective_piston_area) + fs ** 2)

    @staticmethod
    def trunk_resonant_frequency(total_cms, effective_piston_area, trunk_volume, fs):
        # Formula to calculate the resonant frequency for a speaker in the trunk
        return (1 / (2 * 3.141592) * math.sqrt
                (((total_cms + (trunk_volume * 1000)) /
                 effective_piston_area) + fs ** 2))

    @staticmethod
    def cabin_resonant_frequency(total_cms, effective_piston_area, cabin_volume, fs):
        # Formula to calculate the resonant frequency for a speaker in the cabin
        return (1 / (2 * 3.141592) * math.sqrt
                (((total_cms + (cabin_volume * 1000)) /
                  effective_piston_area) + fs ** 2))

    @staticmethod
    def ceiling_resonant_frequency(total_cms, effective_piston_area, ceiling_area, fs):
        # Formula to calculate the resonant frequency for a speaker in the ceiling
        return (1 / (2 * 3.141592) * math.sqrt
                (((total_cms + (ceiling_area * 1000)) /
                  effective_piston_area) + fs ** 2))


class Vented:
    def __init__(self, vas, fs, qts, vb):
        self.vas = vas
        self.fs = fs
        self.qts = qts
        self.vb = vb

    @staticmethod
    def theoretical_cut_off_frequency(self):
        # Formula for calculating the theoretical cut-off frequency
        return 0.26 * self.fs * (self.qts ** -1.4)

    @staticmethod
    def tuning_frequency(self):
        # Formula for calculating the tuning frequency
        return 0.42 * self.fs * (self.qts ** -0.9)

    @staticmethod
    def f3(self, vb):
        # Formula for finding F3
        return ((self.vas / vb) ** 0.5) * self.fs

    @staticmethod
    def new_tuning_frequency(self, vb):
        # Formula for calculating the new tuning frequency
        return ((self.vas / vb) ** 0.32) * self.fs

    @staticmethod
    def port_diameter_for_driver(self):
        # Determine port diameter for drivers in vented and bandpass boxes
        if 6 <= self.driver_diameter <= 8:
            return 3
        elif 8 < self.driver_diameter <= 10:
            return 4
        elif 10 < self.driver_diameter <= 12:
            return 5
        elif 12 < self.driver_diameter <= 15:
            return 6
        elif 15 < self.driver_diameter <= 18:
            return 8
        elif 18 < self.driver_diameter <= 21:
            return 10
        elif 21 < self.driver_diameter <= 26:
            return 16
        elif 26 < self.driver_diameter <= 32:
            return 22

    @staticmethod
    def port_length(vb, fb, port_diameter):
        # Formula for calculating the port length
        port_radius = port_diameter / 2
        vb_cubic_inches = vb * 1728
        return (1.463 * (10 ** 7) * (port_radius ** 2) / (fb ** 2) * vb_cubic_inches) - 1.463 * port_radius

    @staticmethod
    def equivalent_port_diameter(ports_diameters):
        # Calculate equivalent cross-sectional area of multiple ports that will equal a single, larger port
        sum_of_squares = sum(d ** 2 for d in ports_diameters)
        return sum_of_squares ** 0.5


class Enclosures:
    @staticmethod
    def vr(self, vb, vr_ratio):
        # Formula for calculating the volume of Vr chamber
        self.vr = vr_ratio * vb
        return self.vr

    @staticmethod
    def vf(self):
        # Formula for calculating Vf
        return 2 * self.vf

    @staticmethod
    def vf_tuning_frequency(self):
        # Formula for calculating the Vf tuning frequency
        return 0.70 * (self.fs / self.qts)

    @staticmethod
    def enclosure_volume(self):
        # Formula for calculating the enclosure volume
        return 15 * self.vas * (self.qts ** 2.87)

    @staticmethod
    def vb_dual_reflex(vb1, vb2):
        # Formula for calculating the total enclosure volume for dual reflex
        return vb1 + vb2

    @staticmethod
    def qts_dual_reflex(qts1, qts2):
        # Formula for calculating the total Qts for dual reflex
        return (qts1 + qts2) / 2

    @staticmethod
    def f3_dual_reflex(f3_1, f3_2):
        # Formula for calculating the F3 frequency for dual reflex
        return (f3_1 ** 2 + f3_2 ** 2) ** 0.5

    @staticmethod
    def vb_triple_chamber_reflex(vb1, vb2, vb3):
        # Formula for calculating the total enclosure volume for triple chamber reflex
        return vb1 + vb2 + vb3

    @staticmethod
    def f3_triple_chamber_reflex(f3_1, f3_2, f3_3):
        # Formula for calculating the F3 frequency for triple chamber reflex
        return (f3_1 ** 2 + f3_2 ** 2 + f3_3 ** 2) ** 0.5

    @staticmethod
    def qts_triple_chamber_reflex(qts1, qts2, qts3):
        # Formula for calculating the total Qts for triple chamber reflex
        return (qts1 + qts2 + qts3) / 3

    @staticmethod
    def on_off_axis_tuning_frequency(self):
        # Formula for calculating the tuning frequency of on/off axis enclosure
        return 0.38 * self.fs * (self.qts ** -1.1)

    @staticmethod
    def on_off_axis_enclosure_volume(self):
        # Formula for calculating the volume of on/off axis enclosure
        return 10 * self.vas * (self.qts ** 2.5)

    @staticmethod
    def folded_transmission_line_tuning_frequency(self):
        # Formula for calculating the tuning frequency of
        # a folded transmission line enclosure
        return 0.45 * self.fs * (self.qts ** -1.3)

    @staticmethod
    def folded_transmission_line_enclosure_volume(self):
        # Formula for calculating the volume of folded transmission line enclosure
        return 12 * self.vas * (self.qts ** 3)

    @staticmethod
    def quarter_wave_transmission_line_enclosure_volume(self):
        # Formula for calculating the volume of quarter-wave transmission line enclosure
        return 8 * self.vas * (self.qts ** 2)

    @staticmethod
    def quarter_wave_transmission_line_tuning_frequency(self):
        # Formula for calculating the tuning frequency of
        # a quarter-wave transmission line enclosure
        return 0.32 * self.fs * (self.qts ** -0.8)

    @staticmethod
    def tapered_quarter_wave_transmission_line_enclosure_volume(self):
        # Formula for calculating the volume of
        # a tapered quarter-wave transmission line enclosure
        return 14 * self.vas * (self.qts ** 3.5)

    @staticmethod
    def tapered_quarter_wave_transmission_line_tuning_frequency(self):
        # Formula for calculating the tuning frequency of
        # a tapered quarter-wave transmission line enclosure
        return 0.50 * self.fs * (self.qts ** -1.5)

    @staticmethod
    def calculate_dftqwt_resonant_frequency(speed_of_sound, effective_length):
    # Formula to calculate the resonant frequency (Fb) for a dual folded tapered quarter-wave TL
    return speed_of_sound / (4 * effective_length)

    @staticmethod
    def calculate_dftqwt_quarter_wave_point_frequency(speed_of_sound, effective_length):
    # Formula to calculate the quarter-wave point frequency (Fc) for a dual folded tapered quarter-wave TL
    return speed_of_sound / (2 * effective_length)

    def calculate_dftqwt_minus3dB_frequency(speed_of_sound, effective_length, additional_length):
    # Formula to calculate the -3 dB frequency (F3) for a dual folded tapered quarter-wave TL
    return speed_of_sound / (4 * (effective_length + additional_length))

    @staticmethod
    def f3_dual_folded_quarter_wave(f3_1, f3_2):
        # Formula for calculating the F3 frequency for dual folded quarter-wave
        return (f3_1 ** 2 + f3_2 ** 2) ** 0.5

    @staticmethod
    def qts_dual_folded_transmission_line(qts1, qts2):
        # Formula for calculating the total Qts for dual folded transmission line
        return (qts1 + qts2) / 2

    def f3_dual_folded_transmission_line(f31, f32):
        # Formula for calculating the F3 frequency for dual folded transmission line
        return (f31 ** 2 + f32 ** 2) ** 0.5

    @staticmethod
    def qts_dual_folded_quarter_wave(qts1, qts2):
        # Formula for calculating the total Qts for dual folded quarter-wave
        return (qts1 + qts2) / 2

    @staticmethod
    def dual_folded_quarterwave_tuning_frequency(frequency1, frequency2):
        # Formula to calculate the total tuning frequency for dual folded quarter-wave enclosure
        return (frequency1 ** 2 + frequency2 ** 2) ** 0.5

    @staticmethod
    def dual_folded_quarterwave_port_length(port_area, speed_of_sound):
        # Formula to calculate the effective length of the port for dual folded quarter-wave enclosure
        return port_area / speed_of_sound

    @staticmethod
    def calculate_dfqwt_resonant_frequency(speed_of_sound, effective_length):
    # Formula to calculate the resonant frequency (Fb) for a dual folded quarter-wave TL
    return speed_of_sound / (4 * effective_length)

    @staticmethod
    def calculate_dfqwt_quarter_wave_point_frequency(speed_of_sound, effective_length):
    # Formula to calculate the quarter-wave point frequency (Fc) for a dual folded quarter-wave TL
    return speed_of_sound / (2 * effective_length)

    @staticmethod
    def calculate_dfqwt_minus3dB_frequency(speed_of_sound, effective_length, additional_length):
    # Formula to calculate the -3 dB frequency (F3) for a dual folded quarter-wave TL
    return speed_of_sound / (4 * (effective_length + additional_length))


class Sealed:
    @staticmethod
    def optimal_sealed_volume(driver_vas, driver_qts, driver_fs):
        # Formula to calculate the optimal volume for a sealed enclosure
        return 0.9 * driver_vas / ((driver_qts ** 3) * (driver_fs ** 2))

    @staticmethod
    def air_spring_constant(enclosure_volume, driver_qts):
        # Formula to calculate the air spring constant for a sealed enclosure
        return (enclosure_volume * (driver_qts ** 2)) / 845

    @staticmethod
    def cutoff_frequency(enclosure_volume, driver_vas):
        # Formula to calculate the cutoff frequency for a sealed enclosure
        return (enclosure_volume / (driver_vas * 1.464)) ** 0.5

    @staticmethod
    def sealed_qtc(enclosure_volume, driver_vas):
        # Formula to calculate the enclosure Qtc for a sealed enclosure
        return (enclosure_volume / (driver_vas * 1.464)) ** 0.5

    @staticmethod
    def critical_damping_ratio(driver_qts):
        # Formula to calculate the critical damping ratio for a sealed enclosure
        return 0.707 / driver_qts


class Isobaric:
    @staticmethod
    def isobaric(vas, qts):
        # Formula for calculating the enclosure volume for vented isobaric conditions
        return 10 * vas * (qts ** 2.2)

    @staticmethod
    def sealed_compound_volume(vb1,  vb2):
        # Formula to calculate the volume of a compound sealed enclosure
        return vb1 + vb2

    @staticmethod
    def sealed_back_to_back_volume(single_volume):
        # Formula to calculate the volume of a back-to-back sealed enclosure
        return 2 * single_volume

    @staticmethod
    def sealed_planar_volume(surface_area, thickness):
        # Formula to calculate the volume of a planar sealed enclosure
        return surface_area * thickness

    @staticmethod
    def sealed_push_pull_volume(vb1,  vb2):
        # Formula to calculate the volume of a push/pull sealed enclosure
        return vb1 + vb2

    @staticmethod
    def vented_isobaric_tuning_frequency(vas, qts, enclosure_volume):
        # Formula to calculate the tuning frequency for vented enclosure in isobaric conditions
        return 0.42 * (vas / enclosure_volume) * (qts ** -0.9)

    @staticmethod
    def vented_isobaric_cut_off_frequency(fs, qts):
        # Formula to compute the theoretical cut-off frequency for vented enclosure in isobaric conditions
        return 0.26 * fs * (qts ** -1.4)

    @staticmethod
    def vented_isobaric_port_area(tuning_frequency, enclosure_volume):
        # Formula to determine optimal port area for vented enclosure in isobaric conditions
        return 0.224 * (tuning_frequency * enclosure_volume) ** 0.6

    @staticmethod
    def vented_isobaric_port_length(port_area, tuning_frequency, air_density=1.18):
        # Formula to calculate required port length for vented enclosure in isobaric conditions
        return (23562.5 * (port_area ** 2) / (tuning_frequency ** 3)) * (1 / air_density)

    @staticmethod
    def vented_isobaric_air_speed(port_area, tuning_frequency, enclosure_volume):
        # Formula to estimate air speed within the port for vented enclosure in isobaric conditions
        return (port_area * tuning_frequency) / enclosure_volume

    def calculate_efficiency(fb, qts, fs, air_density=1.18):
        # Formula to determine the overall efficiency of vented enclosure in isobaric conditions
        return (0.775 * float(integer) * (fb ** 2) * qts) / (fs * air_density)

class Horns:
    def __init__(self):
        self.con = {'rate_of_flare': "", 'rat_of_flare_constant': ""}
        self.exp = {'rate_of_flare': "", 'rat_of_flare_constant': ""}
        self.hyp = {'rate_of_flare': "", 'rat_of_flare_constant': ""}
        self.par = {'rate_of_flare': "", 'rat_of_flare_constant': ""}
        self.tra = {'rate_of_flare': "", 'rat_of_flare_constant': ""}
        self.ell = {'rate_of_flare': "", 'rat_of_flare_constant': ""}

    def calculate_con_rate_of_flare(self, throat_area, mouth_area, length):
        # Formula for calculating constant directivity horn rate of flare
        self.con['rate_of_flare'] = (mouth_area / throat_area) ** (1 / length)
        return self.con['rate_of_flare']

    def calculate_exp_rate_of_flare(self, throat_area, mouth_area, length):
        # Formula for calculating exponential horn rate of flare
        self.exp['rate_of_flare'] = (mouth_area / throat_area) ** (1 / length)
        return self.exp['rate_of_flare']

    def calculate_hyp_rate_of_flare(self, throat_area, mouth_area, length):
        # Formula for calculating hyperbolic horn rate of flare
        self.hyp['rate_of_flare'] = (mouth_area / throat_area) ** (1 / length)
        return self.hyp['rate_of_flare']

    def calculate_par_rate_of_flare(self, throat_area, mouth_area, length):
        # Formula for calculating parabolic horn rate of flare
        self.par['rate_of_flare'] = (mouth_area / throat_area) ** (1 / length)
        return self.par['rate_of_flare']

    def calculate_tra_rate_of_flare(self, throat_area, mouth_area, length):
        # Formula for calculating tractrix horn rate of flare
        self.tra['rate_of_flare'] = (mouth_area / throat_area) ** (1 / length)
        return self.tra['rate_of_flare']

    def calculate_ell_rate_of_flare(self, throat_area, mouth_area, length):
        # Formula for calculating elliptical horn rate of flare
        self.ell['rate_of_flare'] = (mouth_area / throat_area) ** (1 / length)
        return self.ell['rate_of_flare']

    def calculate_con_rate_of_flare_constant(self, rate_of_flare, throat_area, length):
        # Formula for calculating constant directivity horn rate of flare constant
        self.con['rat_of_flare_constant'] = throat_area * (rate_of_flare ** length)
        return self.con['rat_of_flare_constant']

    def calculate_exp_rate_of_flare_constant(self, rate_of_flare, throat_area, length):
        # Formula for calculating exponential horn rate of flare constant
        self.exp['rat_of_flare_constant'] = throat_area * (rate_of_flare ** length)
        return self.exp['rat_of_flare_constant']

    def calculate_hyp_rate_of_flare_constant(self, rate_of_flare, throat_area, length):
        # Formula for calculating hyperbolic horn rate of flare constant
        self.hyp['rat_of_flare_constant'] = throat_area * (rate_of_flare ** length)
        return self.hyp['rat_of_flare_constant']

    def calculate_par_rate_of_flare_constant(self, rate_of_flare, throat_area, length):
        # Formula for calculating parabolic horn rate of flare constant
        self.par['rat_of_flare_constant'] = throat_area * (rate_of_flare ** length)
        return self.par['rat_of_flare_constant']

    def calculate_tra_rate_of_flare_constant(self, rate_of_flare, throat_area, length):
        # Formula for calculating tractrix horn rate of flare constant
        self.tra['rat_of_flare_constant'] = throat_area * (rate_of_flare ** length)
        return self.tra['rat_of_flare_constant']

    def calculate_ell_rate_of_flare_constant(self, rate_of_flare, throat_area, length):
        # Formula for calculating elliptical horn rate of flare constant
        self.ell['rat_of_flare_constant'] = throat_area * (rate_of_flare ** length)
        return self.ell['rat_of_flare_constant']

    @staticmethod
    def unity_horn_enclosure_volume(self):
        # Formula for calculating the volume of Unity Horn enclosure
        return 16 * self.vas * (self.qts ** 3.2)

    @staticmethod
    def tapped_horn_enclosure_volume(self):
        # Formula for calculating the volume of Tapped Horn enclosure
        return 18 * self.vas * (self.qts ** 3.8)

    @staticmethod
    def wbin_enclosure_volume(self):
        # Formula for calculating the enclosure volume for folded horn (wbin)
        return 10 * self.vb * (self.qts ** 2.87)

    @staticmethod
    def wbin_theoretical_cut_off_frequency(self):
        # Formula for calculating the theoretical cut-off frequency for folded horn (wbin)
        return 0.28 * self.fs * (self.qts ** -1.4)

    @staticmethod
    def wbin_tuning_frequency(self):
        # Formula for calculating the tuning frequency for folded horn (wbin)
        return 0.45 * self.fs * (self.qts ** -0.9)

    @staticmethod
    def wbin_find_f3(self, vb):
        # Formula for finding F3 for folded horn (wbin)
        return ((self.vas / vb) ** 0.5) * self.fs

    @staticmethod
    def wbin_new_tuning_frequency(self, vb):
        # Formula for calculating the new tuning frequency for folded horn (wbin)
        return ((self.vas / vb) ** 0.32) * self.fs

    @staticmethod
    def folded_enclosure_volume(self):
        # Formula for calculating the enclosure volume for folded horn (wbin)
        return 10 * self.vas * (self.qts ** 2.87)

    @staticmethod
    def folded_theoretical_cut_off_frequency(self):
        # Formula for calculating the theoretical cut-off frequency for folded horn (wbin)
        return 0.28 * self.fs * (self.qts ** -1.4)

    @staticmethod
    def folded_tuning_frequency(self, vb):
        # Formula for calculating the tuning frequency for folded horn (wbin)
        return 0.35 * self.fs * (self.qts ** -0.9) * ((self.vas / vb) ** 0.5)

    @staticmethod
    def folded_find_f3(self, vb):
        # Formula for finding F3 for folded horn (wbin)
        return ((self.vas / vb) ** 0.5) * self.fs

    @staticmethod
    def folded_new_tuning_frequency(self, vb):
        # Formula for calculating the new tuning frequency for folded horn (wbin)
        return ((self.vas / vb) ** 0.32) * self.fs


horns = Horns()


class Directivity:
    
    @staticmethod
    def dbsum(levels, axis=None):
        # Energetic summation of levels. Formula:
        # L_{sum} = 10 \\ log_{10}{\\sum_{i=0}^n{10^{L/10}}}
        levels = np.asanyarray(levels)
        return 10.0 * np.log10((10.0 ** (levels / 10.0)).sum(axis=axis))

    @staticmethod
    def dbmean(levels, axis=None):
        # Energetic average of levels. Formula:
        # L_{mean} = 10 \\ log_{10}{\\frac{1}{n}\\sum_{i=0}^n{10^{L/10}}}
        levels = np.asanyarray(levels)
        return 10.0 * np.log10((10.0 ** (levels / 10.0)).mean(axis=axis))

    @staticmethod
    def dbadd(a, b):
        # Energetic addition. Formula:
        # L_{a+b} = 10 \\ log_{10}{10^{L_b/10}+10^{L_a/10}} #
        a = np.asanyarray(a)
        b = np.asanyarray(b)
        return 10.0 * np.log10(10.0 ** (a / 10.0) + 10.0 ** (b / 10.0))

    @staticmethod
    def dbsub(a, b):
        # Energetic subtraction. Formula:
        # L_{a-b} = 10 \\ log_{10}{10^{L_a/10}-10^{L_b/10}} #
        a = np.asanyarray(a)
        b = np.asanyarray(b)
        return 10.0 * np.log10(10.0 ** (a / 10.0) - 10.0 ** (b / 10.0))

    @staticmethod
    def dbmul(levels, f, axis=None):
        # Energetically add `levels` `f` times. Formula:
        # L_{sum} = 10 \\ log_{10}{\sum_{i=0}^n{10^{L/10} \cdot f}} #
        levels = np.asanyarray(levels)
        return 10.0 * np.log10((10.0 ** (levels / 10.0) * f).sum(axis=axis))

    @staticmethod
    def dbdiv(levels, f, axis=None):
        # Energetically divide `levels` `f` times. Formula:
        # L_{sum} = 10 \\ log_{10}{\\sum_{i=0}^n{10^{L/10} / f}} #
        levels = np.asanyarray(levels)
        return 10.0 * np.log10((10.0 ** (levels / 10.0) / f).sum(axis=axis))


__all__ = ['dbsum', 'dbmean', 'dbadd', 'dbsub', 'dbmul', 'dbdiv']

