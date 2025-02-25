import numpy as np
import matplotlib.pyplot as plt

g = 9.8 
v0 = 50
theta = 45

theta_rad = np.radians(theta)

v0x = v0 * np.cos(theta_rad)
v0y = v0 * np.sin(theta_rad)

t_flight = 2 * v0y / g

t = np.linspace(0, t_flight, num=500)

x = v0x * t
y = v0y * t - 0.5 * g * t**2

x= x[y >= 0]
y = y[y >= 0]
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Projectile Path")
plt.title("Projectile Motion")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()
plt.show()