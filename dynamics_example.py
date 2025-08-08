import numpy as np
from dynamics import dynamics
import matplotlib.pyplot as plt

#initials
n = 12 #State vector dimention
m = 6 #Input vector dimention
Ts = 0.1 #Time step
Tstop = 10 #Simulation length in seconds
N = int(Tstop/Ts)
X = np.zeros(shape = (n,1)) #inital conditions vector
T = Tstop #desired terminal time

#Storage
State = []
Input = []


#Main cycle
for j in range(N):

    Uapplied = np.zeros(shape=(m,1))
    # Uapplied[2] = 1 #applying constant signal to the channel responsible for z coordinate
    # Uapplied[3] = 1 #applying constant signal to the channel responsible for phi coordinate

    X,T4 = dynamics(Ts,X,Uapplied,False) #applying only first input vector

    State.append(X) #saving X state vector at j time moment
    Input.append(Uapplied) #saving applied U state vector at j time moment


#plotting the result
fig, axes = plt.subplots(nrows=2, ncols=3)
t = np.arange(0,Tstop,Ts)

plotindex=0
#indexes
# 0 = z
# 2 = x
# 4 = y
# 6 = phi
# 8 = theta
# 10 = psi


axes[0,0].plot(t, np.array(State)[:,plotindex,0], color='red', linewidth=1, markersize=1) 
axes[0,0].set_title('z(t)')
axes[0,0].grid()
axes[0,0].tick_params(axis='both', which='major', pad=15)

plotindex=2
axes[0,1].plot(t, np.array(State)[:,plotindex,0], color='red', linewidth=1, markersize=1) 
axes[0,1].set_title('x(t)')
axes[0,1].grid()
axes[0,1].tick_params(axis='both', which='major', pad=15)

plotindex=4
axes[0,2].plot(t, np.array(State)[:,plotindex,0], color='red', linewidth=1, markersize=1) 
axes[0,2].set_title('y(t)')
axes[0,2].grid()
axes[0,2].tick_params(axis='both', which='major', pad=15)

plotindex=6
axes[1,0].plot(t, np.array(State)[:,plotindex,0], color='red', linewidth=1, markersize=1) 
axes[1,0].set_title('phi(t)')
axes[1,0].grid()
axes[1,0].tick_params(axis='both', which='major', pad=15)

plotindex=8
axes[1,1].plot(t, np.array(State)[:,plotindex,0], color='red', linewidth=1, markersize=1) 
axes[1,1].set_title('theta(t)')
axes[1,1].grid()
axes[1,1].tick_params(axis='both', which='major', pad=15)

plotindex=10
axes[1,2].plot(t, np.array(State)[:,plotindex,0], color='red', linewidth=1, markersize=1) 
axes[1,2].set_title('psi(t)')
axes[1,2].grid()
axes[1,2].tick_params(axis='both', which='major', pad=15)

plt.tight_layout()
plt.show()