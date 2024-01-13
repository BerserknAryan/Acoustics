import numpy as np
import acoustics

class Bands:
    def __init__(self):
        pass

    @staticmethod
    def octave(first, last):
        return acoustics.signal.OctaveBand(fstart=first, fstop=last, fraction=1).nominal

    @staticmethod
    def octave_low(first, last):
        return Bands.octave(first, last) / np.sqrt(2.0)

    @staticmethod
    def octave_high(first, last):
        return Bands.octave(first, last) * np.sqrt(2.0)

    @staticmethod
    def third(first, last):
        return acoustics.signal.OctaveBand(fstart=first, fstop=last, fraction=3).nominal

    @staticmethod
    def third_low(first, last):
        return Bands.third(first, last) / 2.0**(1.0 / 6.0)

    @staticmethod
    def third_high(first, last):
        return Bands.third(first, last) * 2.0**(1.0 / 6.0)

    @staticmethod
    def third2oct(levels, axis=None):
        levels = np.array(levels)
        axis = axis if axis is not None else levels.ndim - 1

        try:
            assert levels.shape[axis] % 3 == 0
        except AssertionError:
            raise ValueError("Wrong shape.")
        shape = list(levels.shape)
        shape[axis] = shape[axis] // 3
        shape.insert(axis + 1, 3)
        levels = np.reshape(levels, shape)
        return np.squeeze(acoustics.decibel.dbsum(levels, axis=axis + 1))

    @staticmethod
    def _check_band_type(freqs):
        octave_bands = Bands.octave(16, 16000)
        third_oct_bands = Bands.third(12.5, 20000)

        def _check_sort(freqs, bands):
            index = np.where(np.in1d(bands, freqs))[0]
            band_pos = index - index[0]
            return (band_pos == np.arange(band_pos.size)).all()

        if np.in1d(freqs, octave_bands).all():
            is_sorted = _check_sort(freqs, octave_bands)
            band_type = "octave" if is_sorted else "octave-unsorted"
        elif np.in1d(freqs, third_oct_bands).all():
            is_sorted = _check_sort(freqs, third_oct_bands)
            band_type = "third" if is_sorted else "third-unsorted"
        else:
            band_type = None

        return band_type
