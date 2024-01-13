# todo: add more enclosures and formulas got suggestions?
import math


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