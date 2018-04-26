import csv
from scipy import signal
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

file_name = 'testovaci.dat'
# nacteni surovych dat
row_count = sum(1 for row in open(file_name))
print(row_count)
raw_data = np.zeros([row_count, 1])
i = 0
with open(file_name) as f:
    reader = csv.reader(f, delimiter="\t")
    col_count = len(next(reader))  # Read first line and count columns
    raw_data = np.zeros([row_count, col_count])
    print(col_count)
f.close()
with open(file_name) as f:
    reader = csv.reader(f, delimiter="\t")
    for line in reader:
        j=0
        for value in line:
           raw_data[i,j] = float(value)
           j = j + 1
        i = i + 1
print(raw_data.shape)
measured_data = raw_data[:, 7:col_count]
fig = plt.figure(1)
ax = fig.gca(projection='3d')
# measured_data = measured_data/np.max(measured_data, axis=0)

# Make data.
X = np.arange(0, col_count-7, 1)
Y = np.arange(0, 15853, 1)
print(X.shape)
print(Y.shape)
print(measured_data.shape)
X, Y = np.meshgrid(X, Y)
# Plot the surface.
surf = ax.plot_surface(X, Y, measured_data, cmap=cm.jet,
                       linewidth=0, antialiased=False, vmin=np.amin(measured_data), vmax=np.amax(measured_data))

fig.colorbar(surf)


channel_data = (measured_data[:, 50]) #95 #180 #100 #25 #50 #55 #75 #85 #93 #1 #195

print(max(channel_data))
fig2 = plt.figure(2)
plt.plot(channel_data)

filtered_channel_data = signal.medfilt(channel_data, 27)
fig3 = plt.figure(3)
plt.plot(filtered_channel_data)
print(channel_data[1000:1020])
print((filtered_channel_data[1000:1020]))

print(max(channel_data))
fig2 = plt.figure(4)

# avg_size = 99
avg_size = 99
avg_channel_data = np.convolve(channel_data, np.ones((avg_size,)) / avg_size, mode ='valid')
avg_channel_data = np.convolve(avg_channel_data, np.ones((avg_size,)) / avg_size, mode ='valid')
avg_channel_data = np.convolve(avg_channel_data, np.ones((avg_size,)) / avg_size, mode ='valid')
# avg_channel_data = np.convolve(avg_channel_data, np.ones((avg_size,)) / avg_size, mode ='valid')
# avg_channel_data = np.convolve(avg_channel_data, np.ones((avg_size,)) / avg_size, mode ='valid')
# avg_channel_data = np.convolve(avg_channel_data, np.ones((avg_size,)) / avg_size, mode ='valid')
# avg_channel_data = np.convolve(avg_channel_data, np.ones((avg_size,)) / avg_size, mode ='valid')

print(avg_channel_data.shape)
estimated_avg = np.average((avg_channel_data[0:avg_size*2]))
# change_point_markers1 = np.where(avg_channel_data > 2 * estimated_avg)
# change_point_markers2 = np.where(avg_channel_data < 0.5 * estimated_avg)
# print(type(change_point_markers1[0]))
# change_point_markers = np.concatenate((change_point_markers1[0],change_point_markers2[0]))
print(estimated_avg)
# print(change_point_markers)
# my_marker = change_point_markers
plt.plot(avg_channel_data, '-g')
np.save('filtrovana_data', avg_channel_data)
plt.show()
