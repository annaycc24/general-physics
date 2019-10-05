from visual import*
from visual.graph import*

ball = sphere(pos=vector(0,0,0), radius=0.00008, color=color.red)
#arrow(pos=vector(0,0,0), shaftwidth=0.1, headwidth=0.3, headlength=0.5)
r=0.001
gdisplay(xtitle="r", ytitle="phiE", ymin=0, ymax=3E-8)
f1=gcurve(color= color.cyan)

dtheta=pi/4
dphi=pi/4
TE=0
for r in arange(0.001,0.01,0.005):
    TE=0
    for theta in arange(0, pi, dtheta):
        for phi in arange(0, pi*2, dphi):
            rv=vector(r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta))
            E=(1/(4*pi*8.854e-12))*(1.6e-19/rv.mag2)*rv.norm()
            arrow(pos=rv, axis=E, shaftwidth=0.00001, color=color.yellow)
            dA=r*dtheta*r*sin(theta)*dphi*rv.norm()
            dTE=dot(E,dA)
            TE+=dTE
            
    #print(TE)
    #print(1.6e-19/8.854e-12)
    f1.plot(pos=(r,TE))
    error=((1.6e-19/8.854e-12)-TE)/(1.6e-19/8.854e-12)
print(error)
