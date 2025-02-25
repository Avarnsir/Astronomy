import numpy as np
import matplotlib.pyplot as plt

#Constants
G = 6.67430e-11 #m^3 kg^-1 s^-2
m1 = 1.989e30 #sun mass
m2 = 5.972e24 #earth mass
dt = 1000 #s
t_max = 365 * 24 * 3600 

#Initial conditions
r1 = np.array([0.0, 0.0])
r2 = np.array([1.496e11, 0.0])
v1 = np.array([0.0, 0.0])
v2 = np.array([0.0, 29783])

#Time array
r1_postions = []
r2_postions = []

#Simulation
for t in np.arange(0, t_max, dt):
    
    #store positions
    r1_postions.append(r1)
    r2_postions.append(r2)
    
    #distance betweem the bodies
    r = r2 - r1
    r_mag = np.linalg.norm(r)
    
    #gravotational force
    F = G * m1 * m2 / r_mag**2
    F_vec = F * r / r_mag

    #update velocities
    v1 += F_vec / m1 * dt
    v2 += -F_vec / m2 * dt

    #update positions
    r1 += v1 * dt
    r2 += v2 * dt
    
    #debug print 
    if t % (1000 * dt) == 0:
        print(f"Time: {t}")
        print(f"Earth position: {r2}")
        print(f"Sun position: {r1}")
        print(f"Gravitational force: {F_vec}")

#create positions to numpy arrays
r1_postions = np.array(r1_postions)
r2_postions = np.array(r2_postions)

#plot the positions
plt.figure(figsize=(8, 8))
plt.plot(r1_postions[:, 0], r1_postions[:, 1], 'yo', label='Sun')
plt.plot(r2_postions[:, 0], r2_postions[:, 1], 'b-', label='Earth')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Two-body simulation')
plt.legend()
plt.grid()
plt.xlim(-2e11, 2e11)
plt.ylim(-2e11, 2e11)
plt.show()