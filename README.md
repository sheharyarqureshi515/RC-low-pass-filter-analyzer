# RC Low-Pass Filter Analyzer

A Python-based analyzer for the frequency response of a first-order RC low-pass filter.

## Circuit Schematic
<img width="990" height="632" alt="image" src="https://github.com/user-attachments/assets/eaec59dd-6c5f-496d-9e2f-4715b6259d69" />

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

fc = 1 / (2πRC)

The magnitude response is:

|H(f)| = 1 / sqrt(1 + (2πfRC)^2)

The phase response is:

φ(f) = -tan⁻¹(2πfRC)

At the cutoff frequency:

- Gain ≈ 0.707
- Magnitude ≈ -3.01 dB
- Phase = -45°

## Technologies

- Python
- NumPy
- Matplotlib
- AutoCAD

## Example

For:

- R = 1 kΩ
- C = 1 µF

The calculated cutoff frequency is approximately:

159.15 Hz

## Gain Response
<img width="640" height="480" alt="Gain Response (RC-Lowpass Filter)" src="https://github.com/user-attachments/assets/c691811e-99eb-4498-a3a8-9c586123f1e1" />

## Bode Magnitude Plot
<img width="640" height="480" alt="Bode Magnitude (RC-Lowpass Filter)" src="https://github.com/user-attachments/assets/ba22850b-d7ce-4829-ba52-1823e413c271" />

## Bode Phase Plot
<img width="640" height="480" alt="Bode Phase (RC-Lowpass Filter)" src="https://github.com/user-attachments/assets/b9efa309-d1a4-4d9d-b887-5acbf80a7bb9" />

