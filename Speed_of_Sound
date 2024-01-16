# acoustics/speed_of_sound.py
import requests

def fetch_speed_of_sound():
    try:
        # Fetch the IP address of the local host
        response = requests.get('https://ipinfo.io')
        data = response.json()
        ip_address = data['ip']

        # Use the IP address to get location-specific data
        location_response = requests.get(f'https://ipinfo.io/{ip_address}')
        location_data = location_response.json()

        # Extract the speed of sound or any other relevant data
        speed_of_sound = int(location_data.get('speed_of_sound', 343))  # Default to 343 if not available

        return speed_of_sound
    except Exception as e:
        print(f"Error fetching speed of sound: {e}")
        return 343  # Default value in case of an error
