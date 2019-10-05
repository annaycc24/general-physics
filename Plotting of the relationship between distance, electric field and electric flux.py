from visual import*
from visual.graph import*
R=0.009 #radius of the ball
ball = sphere(pos=vector(0,0,0), radius=R, color=color.red)
r=0
rp=0
dr=0.0001
drp=R/100
dtheta=pi/19
dphi=pi/19
gdisplay(xtitle="r",ytitle="E")
f2=gcurve(color=color.red)
Q=1.6e-19*1e18
den=Q/((4/3)*pi*R*R*R)
for r in arange(0.0001,0.05,dr):
    rate(1000)
    E=vector(0,0,0)
    rv=vector(r*sin(pi/5)*cos(pi/5), r*sin(pi/5)*sin(pi/5), r*cos(pi/5))

    for rp in arange(0,R, drp):
        for theta in arange(0, pi, dtheta):
            for phi in arange(0, pi*2, dphi):
                rpv=vector(rp*sin(theta)*cos(phi), rp*sin(theta)*sin(phi), rp*cos(theta))
                rm=rv-rpv 
                if rm.mag==0:
                    continue
                dV=rp*rp*sin(theta)*dtheta*dphi*drp
                dE=(1/(4*pi*8.854e-12))*((den*dV)/rm.mag2)*rm.norm()
                E+=dE
    E1=E.mag
    #print(r,E1)
    f2.plot(pos=(r,E1))
