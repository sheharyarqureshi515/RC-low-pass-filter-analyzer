# RC Low-Pass Filter Analyzer

A Python-based analyzer for the frequency response of a first-order RC low-pass filter.

## Circuit Schematic

![RC Low-Pass Filter Schematic](images/rc_filter_schematic.png)

## Features

- Accepts user-defined resistance, capacitance, frequency, and input voltage
- Validates numerical user input
- Calculates:
  - RC time constant
  - Cutoff frequency
  - Capacitive reactance
  - Voltage gain
  - Output voltage
  - Phase shift
- Automatically generates a frequency sweep around the cutoff frequency
- Produces:
  - Gain vs. frequency plot
  - Bode magnitude plot
  - Bode phase plot

## Theory

The cutoff frequency of an RC low-pass filter is:

$$
f_c = \frac{1}{2\pi RC}
$$

The magnitude response is:

$$
|H(f)| = \frac{1}{\sqrt{1 + (2\pi fRC)^2}}
$$

The phase response is:

φ(f) = -tan⁻¹(2πfRC)

At the cutoff frequency:

- Gain ≈ 0.707
- Magnitude ≈ -3 dB
- Phase = -45°

## Example

For:

- R = 1 kΩ
- C = 1 µF

The calculated cutoff frequency is approximately:

159.15 Hz

## Gain Response

![Gain Response](images/gain_response.png)

## Bode Magnitude Plot

![Bode Magnitude Plot](images/bode_magnitude.png)

## Bode Phase Plot

![Bode Phase Plot](images/bode_phase.png)
