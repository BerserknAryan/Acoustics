# example calculation script for using speed of sound

from acoustics.constants import c
from acoustics.speed_of_sound import fetch_speed_of_sound

def calculate_example():
    # Fetch speed of sound
    c = fetch_speed_of_sound()

    # Use the constants and speed of sound for calculations
    result = c / 2  # Example calculation, replace with your actual calculation
    return result
