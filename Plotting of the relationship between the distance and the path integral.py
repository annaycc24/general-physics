#GlowScript 2.7 VPython
R=0.9
#ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=R, thickness=0.01)
m0=4*pi*1e-7
k=m0/(4*pi)
z=vector(0,0,1)
I=(40/110)
dphi=pi/13
drr=0.12
a=0.3
b=0.45
B=vector(0,0,0)
Bf=vector(0,0,0)
gdisplay(xtitle="r",ytitle="path")
f1=gcurve(color=color.red)
rfv=vector(1.5*cos(pi/5),1.5*sin(pi/5),0)
dl=0.01
dlvf=dl*(-z.norm())
dlvn=dl*z.norm()
for rr in arange(0,2,drr):
    rate(100)
    rv=vector(rr*cos(pi/5),rr*sin(pi/5),0)
    for phi in arange (0,2*pi,dphi):
        sv=vector(R*cos(phi),R*sin(phi),0)
        ds=R*dphi*cross(z,sv).norm()                
        r1=rv-sv
        rf1=rfv-sv
        if r1.mag==0:
            continue
        if rf1==0:
            continue
        rn=r1.norm()
        rfn=rf1.norm()
        dB=(k*I)*cross(ds,rn)/(r1.mag2)
        B=dB+B #vector
        B1=B.mag
        dfB=(k*I)*cross(ds,rfn)/(rf1.mag2)
        Bf=dfB+Bf
        Bf1=Bf.mag
    Bs=B-Bf
    BS=dot(Bs,dlvn)
        
        
    #arrow(pos=rv,axis=B,color=color.red,shaftwidth=0.05)
    B=vector(0,0,0)
    Bf=vector(0,0,0)
    f1.plot(pos=(rr,BS))
            #print(rv,B1)
             
