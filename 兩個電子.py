from visual import*
from visual.graph import *
ball1 = sphere(pos=vector(0,0,0), radius=0.00008, color=color.red)
ball2 = sphere(pos=vector(0.002,0,0), radius=0.00008, color=color.red)
#arrow(pos=vector(0,0,0), shaftwidth=0.1, headwidth=0.3, headlength=0.5)
r1=0.002
r2=0.002
R=0
while True:
    for theta in arange(0, pi, pi/30):
        for phi in arange(0, pi*2, pi/30):
            rv1=vector(r1*sin(theta)*cos(phi), r1*sin(theta)*sin(phi), r1*cos(theta))
            rv2=vector(r2*sin(theta)*cos(phi), r2*sin(theta)*sin(phi), r2*cos(theta))
            Rv2=rv2+vector(0.002,0,0)

            E1=(1/(4*pi*8.854e-12))*(1.6e-19/rv1.mag2)*rv1.norm()
            E2=(1/(4*pi*8.854e-12))*(-1.6e-19/rv2.mag2)*Rv2.norm()
            E=E1+E2
            R=rv1+vector(0.001,0,0)
            #arrow(pos=rv1, axis=E1, shaftwidth=0.00001, color=color.yellow)
            #arrow(pos=vector(Rv2), axis=E2, shaftwidth=0.00001, color=color.green)
            #arrow(pos=Rv2, axis=E, shaftwidth=0.00001, color=color.green)
            arrow(pos=R, axis=E, shaftwidth=0.00001, color=color.yellow)
            

    f1 = gcurve(color=color.cyan)# a graphics curve
    f1.plot(pos=(R,E))
    R=R+vector(0.001,0,0)
    while R==vector(0.005,0,0):
        break
