import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 1.989e30     # Mass of galaxy center (e.g., supermassive black hole, kg)
R_s = 3e20       # Scale radius for dark matter (m)
rho_0 = 1e-20    # Central density of dark matter (kg/m^3)

# Define radius range
r = np.logspace(19, 22, 1000)  # Radii from 10^19 to 10^22 meters

# Orbital velocity due to central mass
v_kepler = np.sqrt(G * M / r)

# Orbital velocity due to dark matter halo
v_dark = np.sqrt(4 * np.pi * G * rho_0 * R_s**3 / r) * np.sqrt(np.log(1 + r / R_s) - r / (R_s + r))

# Total orbital velocity
v_total = np.sqrt(v_kepler**2 + v_dark**2)

# Plot the rotation curve
plt.figure(figsize=(10, 6))
plt.loglog(r, v_kepler, label="Keplerian Velocity (Central Mass)")
plt.loglog(r, v_dark, label="Dark Matter Velocity")
plt.loglog(r, v_total, label="Total Velocity")
plt.title("Galaxy Rotation Curve")
plt.xlabel("Radius (m)")
plt.ylabel("Orbital Velocity (m/s)")
plt.legend()
plt.grid()
plt.show()
