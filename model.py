import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
dt = 3600  # Time step in seconds (1 hour)

# Initialize celestial bodies
bodies = {
    "Sun": {"mass": 1.989e30, "pos": np.array([0, 0], dtype=float), "vel": np.array([0, 0], dtype=float)},
    "Earth": {
        "mass": 5.972e24,
        "pos": np.array([1.496e11, 0], dtype=float),  # 1 AU from Sun
        "vel": np.array([0, 29780], dtype=float),    # Orbital speed
    },
    "Mars": {
        "mass": 6.417e23,
        "pos": np.array([2.279e11, 0], dtype=float),  # 1.52 AU from Sun
        "vel": np.array([0, 24077], dtype=float),    # Orbital speed
    },
}

# Compute gravitational force between two bodies
def compute_force(body1, body2):
    r = body2["pos"] - body1["pos"]  # Displacement vector
    distance = np.linalg.norm(r)  # Distance magnitude
    if distance == 0:  # Avoid division by zero
        return np.array([0, 0], dtype=float)
    force_magnitude = G * body1["mass"] * body2["mass"] / distance**2
    force_vector = force_magnitude * (r / distance)  # Unit vector times magnitude
    return force_vector

# Simulation parameters
steps = 100  # Reduce steps for testing; increase for full simulation
positions = {name: [] for name in bodies.keys()}  # Store positions for plotting

# Simulation loop
for step in range(steps):
    forces = {name: np.array([0, 0], dtype=float) for name in bodies.keys()}
    
    # Calculate gravitational forces
    for name1, body1 in bodies.items():
        for name2, body2 in bodies.items():
            if name1 != name2:
                forces[name1] += compute_force(body1, body2)
    
    # Update positions and velocities
    for name, body in bodies.items():
        body["vel"] += (forces[name] / body["mass"]) * dt  # Update velocity
        body["pos"] += body["vel"] * dt  # Update position
        positions[name].append(body["pos"].copy())  # Store position
    
    # Debugging Output
    if step % 10 == 0:  # Print every 10 steps
        print(f"Step {step}:")
        for name, body in bodies.items():
            print(f"  {name}: pos={body['pos']}, vel={body['vel']}")

# Plotting the orbits
plt.figure(figsize=(8, 8))
for name, pos_list in positions.items():
    pos_array = np.array(pos_list)
    plt.plot(pos_array[:, 0], pos_array[:, 1], label=name)

# Formatting the plot
plt.xlabel("x-position (m)")
plt.ylabel("y-position (m)")
plt.title("Orbital Motion of Celestial Bodies")
plt.legend()
plt.grid()
plt.axis('equal')  # Equal scaling for x and y axes
plt.show()

