def unity_horn_enclosure_volume(vas, qts):
    # Formula for calculating the volume of Unity Horn enclosure
    unity_vb = 16 * vas * (qts ** 3.2)
    return unity_vb


def tapped_horn_enclosure_volume(vas, qts):
    # Formula for calculating the volume of Tapped Horn enclosure
    tapped_vb = 18 * vas * (qts ** 3.8) 
    return tapped_vb


def wbin_enclosure_volume(vb, qts):
    # Formula for calculating the enclosure volume for folded horn (wbin)
    wbin_vb = 10 * vb * (qts ** 2.87)
    return wbin_vb


def wbin_theoretical_cut_off_frequency(fs, qts):
    # Formula for calculating the theoretical cut-off frequency for folded horn (wbin)
    wbin_fc = 0.28 * fs * (qts ** -1.4)
    return wbin_fc


def wbin_tuning_frequency(fs, qts, vas, vb):
    # Formula for calculating the tuning frequency for folded horn (wbin)
    wbin_fb = .35 * fs * (qts ** -0.9) * ((vas / vb) ** 0.5)
    return wbin_fb 


def wbin_f3(vas, vb, fs):
    # Formula for finding F3 for folded horn (wbin)
    wbin_f3 = ((vas / vb) ** 0.5) * fs
    return wbin_f3


def wbin_new_tuning_frequency(vb, vas, fs):
    # Formula for calculating the new tuning frequency for folded horn (wbin)
    wbin_new_fb = ((vas / vb) ** 0.32) * fs
    return wbin_new_fb


def folded_enclosure_volume(vas, qts):
    # Formula for calculating the enclosure volume for folded horn (wbin)
    folded_vb = 10 * vas * (qts ** 2.87)
    return folded_vb


def folded_theoretical_cut_off_frequency(fs, qts):
    # Formula for calculating the theoretical cut-off frequency for folded horn (wbin)
    folded_fc = 0.28 * fs * (qts ** -1.4)
    return folded_fc


def folded_tuning_frequency(fs, vb, qts, vas):
    # Formula for calculating the tuning frequency for folded horn (wbin)
    folded_fb = 0.35 * fs * (qts ** -0.9) * ((vas / vb) ** 0.5)
    return folded_fb


def folded_find_f3(vb, vas, fs):
    # Formula for finding F3 for folded horn (wbin)
    folded_f3 = ((vas / vb) ** 0.5) * fs
    return folded_f3


def folded_new_tuning_frequency(vb, vas, fs):
    # Formula for calculating the new tuning frequency for folded horn (wbin)
    folded_new_fb = ((vas / vb) ** 0.32) * fs
    return folded_new_fb
