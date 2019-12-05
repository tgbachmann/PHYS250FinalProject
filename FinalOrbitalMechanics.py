from vpython import *
'''
After numerous failed techniques with the previous methods seen in the jupyter notebooks, I have switched
gears and will now attempt to complete the task through the following method:
'''

# Define constants,parameters
G=6.67408e-11
MS=1.989e+30 # One solar mass
M_BH=50*MS # Black Hole of 5 solar masses
m1=0.001 # mass of particle
m2=0.001 # mass of particle

t=0
dt=5 # dt set to 10 seconds for now

c = 3e8 # speed of light in m/s

R_Sch = (2*G*M_BH)/c**2 # The Schwarzchild radius

k = 1e-6 # Set spring constant to 1 for now
# Don't set spring constant to 1, much too strong, set to 1e-6<k<1e-11 to see how it behaves over the range

Rate_quantity = 100

BlackHole = sphere(pos=vector(0,0,0),radius=R_Sch*1000,color=color.yellow) # radius here only describes how big the
# sphere will appear on the image, not the actual radius of the bh,star,particle, or other object
Particle1 = sphere(pos=vector(0.5*R_Sch*100000,0,0),radius=R_Sch/100000,color=color.blue,make_trail=True)
Particle2 = sphere(pos=vector(0.5*1.005*R_Sch*100000,0,0),radius=R_Sch/100000,color=color.red,make_trail=True)

BlackHole.m = M_BH
Particle1.m = m1
Particle2.m = m2
Particle1.trail = curve(color=Particle1.color)
Particle2.trail = curve(color=Particle2.color)

Particle1.v = vector(0,6.51e5,0)
Particle2.v = vector(0,6.5e5,0)

print(R_Sch*100000,Particle1.pos.x)
print(R_Sch)
#   Loop Begins     #
for i in range(30000):
    rate(Rate_quantity)
    #   Planet Stuff      #
    Particle1_dist = (Particle1.pos.x**2 + Particle1.pos.y**2 + Particle1.pos.z**2)**0.5
    Particle2_dist = (Particle2.pos.x**2 + Particle2.pos.y**2 + Particle2.pos.z**2)**0.5
    Separation = ((Particle2.pos.x-Particle1.pos.x)**2 + (Particle2.pos.y-Particle1.pos.y)**2 + (Particle2.pos.z-Particle1.pos.z)**2)**0.5

    Particle1_magnitude = (Particle1.v.x**2 + Particle1.v.y**2 + Particle1.v.z**2)**0.5
    Particle2_magnitude = (Particle2.v.x**2 + Particle2.v.y**2 + Particle2.v.z**2)**0.5

    Particle1_radial_vector = (BlackHole.pos - Particle1.pos)/Particle1_dist # Unit vector pointing from particle to BH
    Particle2_radial_vector = (BlackHole.pos - Particle2.pos)/Particle2_dist # Unit vector pointing from particle to BH
    Spring_vector1 = (Particle2.pos - Particle1.pos)/Separation # Unit vector pointing from P1 to P2
    Spring_vector2 = (Particle1.pos - Particle2.pos)/Separation # Unit vector point from P2 to P1

    Particle1_Fgrav = G*BlackHole.m*Particle1.m*Particle1_radial_vector/Particle1_dist**2 # Gravity
    Particle2_Fgrav = G*BlackHole.m*Particle2.m*Particle2_radial_vector/Particle2_dist**2 # Gravity
    Particle1_Fspring = k*Separation*Spring_vector1 # Hooke's Law
    Particle2_Fspring = k*Separation*Spring_vector2 # Hooke's Law
    Particle1_Fnet = Particle1_Fgrav + Particle1_Fspring # Net Force
    Particle2_Fnet = Particle2_Fgrav + Particle2_Fspring # Net Force

    Particle1_Acc_grav = Particle1_Fnet/Particle1.m
    Particle2_Acc_grav = Particle2_Fnet/Particle2.m

    Particle1_dV = Particle1_Acc_grav * dt
    Particle2_dV = Particle2_Acc_grav * dt

    Particle1.v += Particle1_dV
    Particle2.v += Particle2_dV

    Particle1_dD = Particle1.v * dt
    Particle2_dD = Particle2.v * dt

    Particle1.pos += Particle1_dD
    Particle2.pos += Particle2_dD

    t += dt
