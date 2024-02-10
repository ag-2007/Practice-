import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

pi= np.pi

#print(np.sin(pi/2))
#print(np.tan(pi))

x = np.arange(1,11)
y = np.arange(10,110,10)

x_sin = np.arange(0,2*pi,0.1)
y_sin = np.sin(x_sin)

x_cosin = np.arange(0,2*pi,0.1)
y_cosin = np.cos(x_cosin)

plt.figure(figsize=(6,6))
plt.subplot(2,2,1)
plt.plot(x_sin,y_sin, 'r-')
plt.title('The Sine Warriors')

plt.subplot(2,2,2)
plt.plot(x_cosin,y_cosin,'g-')
plt.title('The Cosine Warriors')

plt.show()

#can be repeated with tan and cot
