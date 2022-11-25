# import necessary libraries
import matplotlib.pyplot as plt

%matplotlib inline

# initialize lists containing values
x = []
y = []


# define system in terms of separated differential equations

N = 100 #total population in OC in 2021 census
a = 0.84 # infection rate 
b =0.4 # treatment rate, 
w = 0.265 # immunity loss rate 
Q = .84/100 #a/N

def f(x,y):
    return w*(100-x-y)-Q*x*y
def g(x,y):
    return Q*x*y - b*y

#lets start with initial values of (S,I)=(148883, 1)
#set delta to randomly be 3 days
#time range across 2 years, 2020-21

#iv1, iv2 = initial values, dt = timestep, time = range
def sys(iv1, iv2, dt, time):
    # initial values:
    x.append(iv1)
    y.append(iv2)
    # compute and fill lists
    for i in range(time):
        x.append(x[i] + (f(x[i],y[i])) * dt)
        y.append(y[i] + (g(x[i],y[i])) * dt)
        #z.append(z[i] + (h(x[i],y[i],z[i])) * dt)
    return x, y

sys(95, 5, 4.1, 100)

#plot
fig = plt.figure(figsize=(15,5))
fig.subplots_adjust(wspace = 0.5, hspace = 0.3)
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(x, 'r-', label='Susceptible Class')
ax1.plot(y, 'b-', label='Infective Class')
ax1.set_title("Dynamics in time")
ax1.set_xlabel("time (days)")
ax1.grid()
ax1.legend(loc='best')

ax2.plot(x, y, color="blue")
ax2.set_xlabel("Susceptible")
ax2.set_ylabel("Infective")  
ax2.set_title("Phase space")
ax2.grid()
