from vpython import *

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M = 5.972e24      # Mass of the planet (in kg)
m = 1000          # Mass of the satellite (in kg)
r_initial = 7.0e6  # Initial orbital radius (in meters)

# Initial conditions
v_initial = 1000  # Initial velocity (in m/s)

# Create the planet (stationary at the origin)
planet = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.blue, opacity=0.7)

# Create the satellite
satellite = sphere(pos=vector(r_initial, 0, 0), radius=100, color=color.red, make_trail=True)

# Initial velocity vector
satellite.velocity = vector(0, v_initial, 0)

# Set up the graph
graph1 = graph(title="Orbital Motion", xtitle="Radius (m)", ytitle="Angular Momentum (kg m^2/s)")
L_curve = gcurve(color=color.red)

# Time step for the simulation
dt = 60  # 1 minute time step

# Simulation loop
while True:
    rate(50)  # Rate of the simulation (frames per second)

    # Compute the gravitational force
    r = satellite.pos - planet.pos  # Vector from planet to satellite
    r_mag = mag(r)  # Magnitude of the position vector
    F_gravity = -G * M * m / r_mag**2  # Gravitational force magnitude
    force = F_gravity * norm(r)  # Force vector (in direction of r)

    # Update the velocity and position of the satellite
    satellite.velocity += force / m * dt  # F = ma -> a = F/m
    satellite.pos += satellite.velocity * dt  # Update position based on velocity

    # Calculate angular momentum (L = m * r x v)
    angular_momentum = m * mag(cross(r, satellite.velocity))  # Cross product of r and v
    L_curve.plot(r_mag, angular_momentum)  # Plot L vs r

    # Optionally, you can break the loop at any point (e.g., after a certain condition)
    if r_mag > 1e8:  # Example: stop the simulation if the satellite is too far away
        break

