import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

w=np.linspace(-100000.0,100000.0,1000000)
x=np.zeros(len(w))
y=np.zeros(len(w))
for i in range(len(w)):
	x[i]=-((np.pi)/w[i])*(np.sin(0.25*w[i]))
	y[i]=-((np.pi)/w[i])*(np.cos(0.25*w[i]))
	
y1=np.linspace(-1,1,100)
x1=np.zeros(100)
for i in range(len(x1)):
	x1[i]=-0.5

plt.ylim(-1,1)
plt.plot(x,y)
plt.grid()
plt.xlabel("real axis")
plt.ylabel("imaginary axis")
plt.title("nyquist plot")

plt.annotate('(-0.5,0)', xy=(-0.5, 0), xytext=(-0.5,0)),
            
#plt.show()
#if using termux
plt.savefig('./figs/nyquist_cut_real.pdf')
plt.savefig('./figs/nyquist_cut_real.eps')
subprocess.run(shlex.split("termux-open ./figs/nyquist_cut_real.pdf"))
