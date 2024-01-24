import math


# class for dual folded quarterwave transmission lines
class DFQWTL:
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