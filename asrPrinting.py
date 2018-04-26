import numpy as np
import matplotlib.pylab as plt

# load data
usedGevWindow = 1000
endPoint = 14000
data = np.load('hpp_data'+str(usedGevWindow)+'.npy')
d = np.load('filtrovana_data.npy')
hpplog = np.log10(data[0:endPoint-usedGevWindow])

plt.figure(4)
plt.plot(d[:endPoint])
plt.xlabel('k [-]')
plt.ylabel('XRD [-]')


plt.figure(5)
plt.plot(hpplog)
plt.title('hpp2')
x_axe = range(usedGevWindow,endPoint)
print(np.where(data == 0)[0])

data_print = np.sum(hpplog, axis=1)
plt.figure(6)
plt.subplot(211)
plt.plot(x_axe, data_print)

plt.title('sddruzena')
plt.subplot(212)
plt.plot(x_axe, d[usedGevWindow:endPoint])
plt.show()

print('minimum:', min(data_print[0:endPoint]))
print('minimum index:', np.argmin(data_print[0:endPoint]))
wtf = d[usedGevWindow:endPoint]
print(wtf.shape)
print(data_print.shape)
print(d.shape)