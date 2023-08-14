
# Radio Signal Intensity Calculator

This simple Python program calculates the intensity of a radio signal using the inverse square law. Given a user-input distance from the source of the radio signal, the program calculates the intensity in nanowatts (nW) based on predefined values for other parameters.

## Prerequisites

To run this program, you'll need:

- Python 3.x installed on your machine.

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the program by executing the following command:

   ```bash
   python radio_intensity_calculator.py
   ```

4. Enter the distance from the source of the radio signal when prompted.

5. The program will calculate and display the intensity of the radio signal in nanowatts (nW).

## Parameters

The program uses the following parameters for the calculation:

- Transmitted Power: 10 watts
- Transmitting Antenna Gain: 5
- Receiving Antenna Gain: 3
- Wavelength: 0.2 meters

## Formula

The intensity of the radio signal is calculated using the formula:

\[ I = \frac{P_t G_t G_r \lambda^2}{(4\pi)^2 r^2} \]

Where:
- \( I \) is the received power density (intensity) of the radio signal.
- \( P_t \) is the transmitted power.
- \( G_t \) is the gain of the transmitting antenna.
- \( G_r \) is the gain of the receiving antenna.
- \( \lambda \) is the wavelength of the radio signal.
- \( r \) is the distance between the antennas.
- \( \pi \) is a constant approximately equal to 3.14159.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.