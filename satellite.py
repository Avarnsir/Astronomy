import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# Constants
G = 6.67430e-11  # Gravitational constant in m^3/kg/s^2
M = 5.972e24     # Mass of the Earth in kg

def effective_potential(L, m):
    # Define the range of r (distance from Earth's center)
    r = np.linspace(6.4e6, 1e8, 1000)  # From Earth's radius to 100,000 km
    
    # Calculate the effective potential
    V_eff = -G * M * m / r + L**2 / (2 * m * r**2)
    
    # Plot the graph
    plt.figure(figsize=(8, 6))
    plt.plot(r / 1e6, V_eff / 1e9, label=f"L={L:.1e} kg·m²/s, m={m:.1f} kg")
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.title("Effective Potential vs Distance from Earth", fontsize=16)
    plt.xlabel("Distance from Earth (r) in 10⁶ meters", fontsize=14)
    plt.ylabel("Effective Potential (V_eff) in 10⁹ J", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()

# Interactive sliders for L and m (with finer float controls)
interact(effective_potential,
         L=FloatSlider(value=1e10, min=1e9, max=1e11, step=1e9, description="Angular Momentum (L)"),
         m=FloatSlider(value=500.0, min=100.0, max=1000.0, step=50.0, description="Mass of Satellite (m)"))

