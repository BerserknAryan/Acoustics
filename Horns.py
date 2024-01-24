# todo's add abililty to visualize horn shape while designing
# implement ability to split horn into as many segments as wanted
#implement ability to mix multiple flares together
# add radial biradial and others
import math


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