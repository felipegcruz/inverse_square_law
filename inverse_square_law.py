import math

def calculate_radio_intensity(distance):
    if distance <=0:
        raise ValueError("Distance must be greater than zero")
    
    transmitted_power = 10.0 # Transmited power in watts
    transmitted_antenna_gain = 5.0 # Gain of the transmitting antenna
    receiving_antena_gain = 3.0 # Gain of the receiving antenna
    wavelength = 0.2 # Wavelength in meters

    intensity_watts = (transmitted_power * transmitted_antenna_gain * receiving_antena_gain * wavelength ** 2) / ((4 * math.pi) ** 2 * distance ** 2)
    intensity_nW = intensity_watts * 1e9 # Convert to nanowatts
    return intensity_nW

distance = float(input("Enter the distance from the source (meters): "))

intensity = calculate_radio_intensity(distance)
print(f"The intensity of the radio signal is: {intensity:.2f} nW")
