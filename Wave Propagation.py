import math

def soundwave_propagation_model(x, t, P_max, k, omega, phi, s_max):
    # Modeling pressure wave
    delta_P = P_max * math.sin(k * x - omega * t + phi)
    
    # Modeling air molecule displacement
    displacement = s_max * math.cos(k * x - omega * t + phi)
    
    return delta_P, displacement