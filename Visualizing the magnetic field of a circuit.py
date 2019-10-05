GlowScript 2.7 VPython
R=0.9
ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=R, thickness=0.01)
m0=4*pi*1e-7
k=m0/(4*pi)
z=vector(0,0,1)
I=(40/110)*1e06
dphi=pi/13
dr=0.111
B=vector(0,0,0)
f1=gcurve(color=color.red)
for Z in arange(-1,1,0.1):
    for rr in arange(0,1.5,0.5):
        for phi1 in arange(0,2*pi,pi/4):
            rate(100)
            rv=vector(rr*cos(phi1),rr*sin(phi1),Z)
            for phi in arange (0,2*pi,dphi):
                sv=vector(R*cos(phi),R*sin(phi),0)
                svn=sv.norm()
                ds=R*dphi*cross(z,svn)
                sd=(pos=vector(sv))
                rd=(pos=vector(rv))                
                r1=rd-sd
                if r1.mag==0:
                    continue
                rn=r1.norm()
                dB=(k*I)*cross(ds,rn)/(r1.mag2)
                B=dB+B #vector
                B1=B.mag
            arrow(pos=rv,axis=B,color=color.white,shaftwidth=0.01)
    #f1.plot(pos=(r,B1))
            #print(rv,B1)
            B=vector(0,0,0)
