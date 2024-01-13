# todo: add more enclosures and formulas got suggestions?
import math
from formulas import constants
from acoustics.constants import c


class Enclosures:
    @staticmethod
    def vr(vb, vr_ratio):
        # Formula for calculating the volume of Vr chamber
        return vr_ratio * vb

    @staticmethod
    def vf(vb):
        # Formula for calculating Vf
        return 'Vf': lambda vb: vb / 2  


    @staticmethod
    def vf_tuning_frequency(fs, qts):
        # Formula for calculating the Vf tuning frequency
        return 'Vf_tuning_frequency': lambda fs, qts: 0.70 * (fs / qts)

    @staticmethod
    def enclosure_volume(vas, qts):
        # Formula for calculating the enclosure volume
        return 'Enclosure_Volume': lambda vas, qts:15 * vas * (qts ** 2.87)

    @staticmethod
    def vb_effective_port_volume(vb, vp):
        # Example formula, adjust as needed
        return 'Vb_effective_port_volume': lambda vb, vp: vb + vp
        
    @staticmethod
    def vb_dual_reflex(vb1, vb2):
        # Formula for calculating the total enclosure volume for dual reflex
        return 'Vb_dual_reflex_enclosure': lambda vb1, vb2: vb1 + vb2

    @staticmethod
    def qts_dual_reflex(qts1, qts2):
        # Formula for calculating the total Qts for dual reflex
        return 'Qts_dual_reflex_enclosure': lambda qts1, qts2: (qts1 + qts2) / 2

    @staticmethod
    def f3_dual_reflex(f31, f32):
        # Formula for calculating the F3 frequency for dual reflex
        return 'F3_dual_reflex': lambda f31, f32: (f31 ** 2 + f32 ** 2) ** 0.5

    @staticmethod
    def vb_triple_chamber_reflex(vb1, vb2, vb3):
        # Formula for calculating the total enclosure volume for triple chamber reflex
        return 'Vb_triple_reflex': lambda vb1, vb2, vb3: vb1 + vb2 + vb3

    @staticmethod
    def f3_triple_chamber_reflex(f31, f32, f33):
        # Formula for calculating the F3 frequency for triple chamber reflex
        return 'f3_triple_reflex': lambda f31, f32, f33: (f31 ** 2 + f32 ** 2 + f33 ** 2) ** 0.5

    @staticmethod
    def qts_triple_chamber_reflex(qtc1, qtc2, qtc3):
        # Formula for calculating the total Qts for triple chamber reflex
        return 'Qtc_triple_reflex': lambda qtc1, qtc2, qtc3: (qtc1 + qtc2 + qtc3) / 3


    @staticmethod
    def on_off_axis_tuning_frequency(fs, qts):
        # Formula for calculating the tuning frequency of on/off axis enclosure
        return 'On_Off_axis_tuning': lambda fs, qts: 0.38 * fs * (qts ** -1.1)

    @staticmethod
    def on_off_axis_enclosure_volume(vas, qts):
        # Formula for calculating the volume of on/off axis enclosure
        return 'On_Off_axis_vb': lambda vas, qts: 10 * vas * (qts ** 2.5)

    @staticmethod
    def folded_transmission_line_tuning_frequency(fs, qts):
        # Formula for calculating the tuning frequency of
        # a folded transmission line enclosure
        return 'folded_TL_tuning': lambda fs, qts: 0.45 * fs * (qts ** -1.3)

    @staticmethod
    def folded_transmission_line_enclosure_volume(vas, qts):
        # Formula for calculating the volume of folded transmission line enclosure
        return 'Folded_TL_Vb': lambda vas, qts: 12 * vas * (qts ** 3)

    @staticmethod
    def quarter_wave_transmission_line_enclosure_volume(vas, qts):
        # Formula for calculating the volume of quarter-wave transmission line enclosure
        return 'QWTL_Vb': lambda vas, qts: 8 * vas * (qts ** 2)

    @staticmethod
    def quarter_wave_transmission_line_tuning_frequency(fs, qts):
        # Formula for calculating the tuning frequency of
        # a quarter-wave transmission line enclosure
        return 'QWTL_tuning': lambda fs, qts: 0.32 * fs * (qts ** -0.8)

    @staticmethod
    def tapered_quarter_wave_transmission_line_enclosure_volume(vas, qts):
        # Formula for calculating the volume of
        # a tapered quarter-wave transmission line enclosure
        return 'TQWTL_Vb': lambda vas, qts: 14 * vas * (qts ** 3.5)

    @staticmethod
    def tapered_quarter_wave_transmission_line_tuning_frequency(fs, qts):
        # Formula for calculating the tuning frequency of
        # a tapered quarter-wave transmission line enclosure
        return 'TQWTL_tuning': lambda fs, qts: 0.50 * fs * (qts ** -1.5)

    @staticmethod
    def dfqwtl_resonant_frequency(c, effective_length):
        # Formula to calculate the resonant frequency (Fb) for a dual folded tapered quarter-wave TL
        return 'DFQWTL_resonant': lambda c: c / (4 * effective_length)

    @staticmethod
    def dftqwt_quarter_wave_point_frequency(c, effective_length):
        # Formula to calculate the quarter-wave point frequency (Fc) for a dual folded tapered quarter-wave TL
        return c / (2 * effective_length)

    @staticmethod
    def dftqwt_minus3dB_frequency(c, effective_length, additional_length):
        # Formula to calculate the -3 dB frequency (F3) for a dual folded tapered quarter-wave TL
        return c / (4 * (effective_length + additional_length))

    @staticmethod
    def dfqwtl_f3(f31, f32):
        # Formula for calculating the F3 frequency for dual folded quarter-wave
        return (f31 ** 2 + f32 ** 2) ** 0.5

    @staticmethod
    def dual_folded_transmission_line_qts(qts1, qts2):
        # Formula for calculating the total Qts for dual folded transmission line
        return (qts1 + qts2) / 2

    def dual_folded_transmission_line_f3(f31, f32):
        # Formula for calculating the F3 frequency for dual folded transmission line
        return (f31 ** 2 + f32 ** 2) ** 0.5

    @staticmethod
    def dual_folded_quarter_wave_f3(qts1, qts2):
        # Formula for calculating the total Qts for dual folded quarter-wave
        return (qts1 + qts2) / 2

    @staticmethod
    def dual_folded_quarterwave_tuning_frequency(frequency1, frequency2):
        # Formula to calculate the total tuning frequency for dual folded quarter-wave enclosure
        return (frequency1 ** 2 + frequency2 ** 2) ** 0.5

    @staticmethod
    def dual_folded_quarterwave_port_length(port_area, c):
        # Formula to calculate the effective length of the port for dual folded quarter-wave enclosure
        return 'DFWQ_port_length': lambda c: port_area / c

    @staticmethod
    def dual_folded_quarterwave_resonant_frequency(c):
        # formula to find Fb of a dual folded qw resonator+
        return 'DFQW_Fb': lambda c: c / (4 * wavelength)
        
    @staticmethod
    def dual_folded_quarterwave_port_area(c, fb):