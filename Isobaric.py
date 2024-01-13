# todo: implement into a function callable to other systems instead of needing other system calculations
import math


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