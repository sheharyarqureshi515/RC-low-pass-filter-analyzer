# =========================
# Imports
# =========================

import math                         # standard mathematical functions and constants
import numpy as np                  # numerical arrays and vectorized calculations
import matplotlib.pyplot as plt     # plotting and graph generation

# =========================
# Input validation
# =========================

# Ensures that users enter a valid positive number
def value_check(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value
            else:
                print("Value must be greater than 0.")

        except ValueError:
            # Input could not be converted to a floating-point number
            print("Enter a valid value")

# =========================
# RC Filter Calculations
# =========================

def calculate_time_constant(R, C):
    time_constant = R * C
    return time_constant

def calculate_cutoff_frequency(time_constant):
    cutoff_freq = 1/(2*math.pi*time_constant)
    return cutoff_freq

def calculate_capacitive_reactance(f, C):
    capacitor_reactance = 1/(2*math.pi*f*C)
    return capacitor_reactance

def calculate_gain(f, time_constant):
    gain = 1/math.sqrt(1 + (2*math.pi*f*time_constant)**2)
    return gain

def calculate_output_voltage(Vin, gain):
    Vout = Vin * gain
    return Vout

def calculate_phase(f, time_constant):
    angle_radians = -np.arctan(2 * np.pi * f * time_constant)
    angle_degrees = np.degrees(angle_radians)
    return angle_degrees

def calculate_frequency_response(freq, time_constant):
    gain = 1/np.sqrt(1 + (2*np.pi*freq*time_constant)**2)
    return gain

# =========================
# Plotting Functions
# =========================

# Plot gain against frequency

def plot_gain_response(frequencies, frequency_gain, cutoff_freq):
    plt.figure()

    plt.semilogx(frequencies, frequency_gain)

    plt.axvline(
        cutoff_freq,
        linestyle="--",
        label=f"Cutoff Frequency = {cutoff_freq:.2f} Hz"
    )

    plt.axhline(
        1 / math.sqrt(2),
        linestyle="--",
        label="Cutoff Gain = 0.707"
    )

    plt.title("RC Low-Pass Filter Gain vs Frequency")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain |H(f)|")
    plt.grid(True)
    plt.legend() 

# Plot Bode magnitude against frequency

def plot_bode_magnitude(frequencies, gain_dB, cutoff_freq):
    plt.figure()

    plt.semilogx(frequencies, gain_dB)

    plt.axvline(
        cutoff_freq,
        linestyle="--",
        label=f"Cutoff Frequency = {cutoff_freq:.2f} Hz"
    )

    plt.axhline(
        -3.01,
        linestyle="--",
        label="Cutoff Magnitude = -3.01 dB"
    )

    plt.title("RC Low-Pass Filter Bode Magnitude Plot")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.legend()

# Plot the phase against frequency

def plot_bode_phase(frequencies, phase_response, cutoff_freq):
    plt.figure()

    plt.semilogx(frequencies, phase_response)

    plt.axvline(
        cutoff_freq,
        linestyle="--",
        label=f"Cutoff Frequency = {cutoff_freq:.2f} Hz"
    )

    plt.axhline(
        -45,
        linestyle="--",
        label="Phase at Cutoff = -45°"
    )

    plt.title("RC Low-Pass Filter Bode Phase Plot")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (Degrees)")
    plt.grid(True)
    plt.legend()

# =========================
# User Inputs
# =========================

resistance = value_check("Enter resistance (ohms): ")
capacitance = value_check("Enter capacitance (farads): ")
frequency = value_check("Enter frequency (Hz): ")
input_voltage = value_check("Enter input voltage (V): ")

# =========================
# Filter Analysis
# =========================

time_constant = calculate_time_constant(resistance, capacitance)
gain = calculate_gain(frequency, time_constant)
cutoff_freq = calculate_cutoff_frequency(time_constant)

# Generate 500 logarithmically spaced frequencies from
# two decades below to two decades above the cutoff frequency
frequencies = np.logspace(
    np.log10(cutoff_freq) - 2,
    np.log10(cutoff_freq) + 2,
    500
)

Vout = calculate_output_voltage(input_voltage, gain)
phase_response = calculate_phase(frequencies, time_constant)
phase_angle = calculate_phase(frequency, time_constant)
frequency_gain = calculate_frequency_response(frequencies, time_constant)

# Convert voltage gain ratio to decibels
gain_dB = 20 * np.log10(frequency_gain)

# =========================
# Display Results
# =========================

print("\n--- RC Low-Pass Filter Results ---")
print(f"Time Constant: {time_constant:.6f} s")
print(f"Cutoff Frequency: {cutoff_freq:.2f} Hz")
print(f"Capacitive Reactance at {frequency:.2f} Hz: "
      f"{calculate_capacitive_reactance(frequency, capacitance):.2f} ohms")
print(f"Gain at {frequency:.2f} Hz: {gain:.4f}")
print(f"Output Voltage: {Vout:.4f} V")
print(f"Phase Shift: {phase_angle:.2f} degrees")

# =========================
# Generate Plots
# =========================

plot_gain_response(
    frequencies,
    frequency_gain,
    cutoff_freq
)

plot_bode_magnitude(
    frequencies,
    gain_dB,
    cutoff_freq
)

plot_bode_phase(
    frequencies,
    phase_response,
    cutoff_freq
)

plt.show()