# todo's add abililty to visualize horn shape while designing
# implement ability to split horn into as many segments as wanted
# implement ability to mix multiple flares together
# add radial biradial and others
import math


class Horns:
    @staticmethod
    def calculate_hyp_rate_of_flare(at, amt, length):
        return (math.pi * at ** 2) / (1 + (2 / (math.exp((2 * length) / (at * amt))) - 1))

    @staticmethod
    def calculate_hyp_rate_of_flare_constant(rate_of_flare, at, ax):
        return (2 * math.atan(rate_of_flare * ax / (2 * at)) - 2 * math.atan
                (rate_of_flare * 0 / (2 * at)))

    @staticmethod
    def calculate_par_rate_of_flare(at, amt, length):
        return (4 * amt) / (math.pi * at)

    @staticmethod
    def calculate_par_rate_of_flare_constant(rate_of_flare, at, ax):
        return (2 * math.atan(rate_of_flare * ax / (2 * at)) - 2 * math.atan
                (rate_of_flare * 0 / (2 * at)))

    @staticmethod
    def calculate_tra_rate_of_flare(at, amt, length):
        return amt * (math.exp((amt * length) / at) - 1)

    @staticmethod
    def calculate_tra_rate_of_flare_constant(rate_of_flare, at, ax):
        return (2 * math.atan(rate_of_flare * ax / (2 * at)) - 2 * math.atan
                (rate_of_flare * 0 / (2 * at)))

    @staticmethod
    def calculate_ell_rate_of_flare(at, amt, length):
        return 2 * (math.atan(amt * length / (2 * at)) - math.atan
                    (amt * 0 / (2 * at))) / ax

    @staticmethod
    def calculate_ell_rate_of_flare_constant(rate_of_flare, at, ax):
        return 2 * math.atan(rate_of_flare * ax / (2 * at)) - 2 * math.atan(rate_of_flare * 0 / (2 * at))

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