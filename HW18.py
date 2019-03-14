#Mary-Ellen Phillips

#excel read
import pandas as pd
t1 = pd.read_excel('data_tasks.xlsx',sheet_name='task1')
t2 = pd.read_excel('data_tasks.xlsx',sheet_name='task2')

#Imagine you are asked to present these data in a poster (at lest 600 dpi for 
#each figure). Use both the line chart and the bar chart to plot these data 
#properly. The font of labels, legends, axis ticks, etc, embedded in the figure 
#must be readable. The line width must be adjusted to a proper thickness. 

#Task1
print('Task 1')

timePoint = t1.values[:,0]
temp = t1.values[:,1]
stdDev = t1.values[:,2]

import matplotlib.pyplot as plt

#   Line Chart
plt.errorbar(timePoint,temp,yerr = stdDev,fmt = "rs--",
             linewidth = 2.5,elinewidth = 1, ecolor = 'k',
             capsize = 5, capthick = 1)
plt.title('Temperature vs. Time', fontsize = 15)
plt.xlabel('Time (minutes)', fontsize = 11)
plt.ylabel('Temperature (C)', fontsize = 11)
plt.savefig('lineChart1.png',dpi = 600)
plt.show()

#   Bar Chart
plt.bar(timePoint,temp, yerr = stdDev, align = "center",
        ecolor = 'black', capsize = 10)
plt.title('Temperature vs. Time', fontsize = 15)
plt.xlabel('Time (minutes)', fontsize = 11)
plt.ylabel('Temperature (C)', fontsize = 11)
plt.savefig('barChart1.png', dpi = 600)
plt.show()

#Task2
print('Task 2')

timePoint = t2.values[1:,0]
temp_LV = t2.values[1:,1]
stdDev_LV = t2.values[1:,2]
temp_DGO = t2.values[1:,3]
stdDev_DGO = t2.values[1:,4]
temp_DV = t2.values[1:,5]
stdDev_DV = t2.values[1:,6]

#   Line Chart

plt.errorbar(timePoint,temp_LV,yerr = stdDev_LV,fmt = "rs--",
             linewidth = 2.5,elinewidth = 1, ecolor = 'k',
             capsize = 5, capthick = 1)
plt.errorbar(timePoint,temp_DGO,yerr = stdDev_DGO,fmt = "bs--",
             linewidth = 2.5,elinewidth = 1, ecolor = 'k',
             capsize = 5, capthick = 1)
plt.errorbar(timePoint,temp_DV,yerr = stdDev_DV,fmt = "gs--",
             linewidth = 2.5,elinewidth = 1, ecolor = 'k',
             capsize = 5, capthick = 1)
plt.title('Temperature vs. Time', fontsize = 15)
plt.xlabel('Time (hours)', fontsize = 11)
plt.ylabel('Temperature (C)', fontsize = 11)
plt.savefig('lineChart2.png',dpi = 600)
plt.legend(['Las Vegas','Durango','Denver'],loc = 'upper left',fontsize = 8.5)
plt.show()

#   Bar Chart

import numpy as np

barWidth = 0.25
r1 = np.arange(len(temp_LV))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1,temp_LV, color = 'red', width = barWidth, edgecolor = 'white', yerr = stdDev_LV, align = "center",
        ecolor = 'black', capsize = 5)
plt.bar(r2,temp_DGO, color = 'blue', width = barWidth, edgecolor = 'white', yerr = stdDev_DGO, align = "center",
        ecolor = 'black', capsize = 5)
plt.bar(r3,temp_DV, color = 'green', width = barWidth, edgecolor = 'white', yerr = stdDev_DV, align = "center",
        ecolor = 'black', capsize = 5)
plt.xticks([r + barWidth for r in range(len(temp_LV))],timePoint)
plt.title('Temperature vs. Time', fontsize = 15)
plt.xlabel('Time (hours)', fontsize = 11)
plt.ylabel('Temperature (C)', fontsize = 11)
plt.savefig('barChart2.png', dpi = 600)
plt.legend(['Las Vegas','Durango','Denver'],loc = 'upper left',fontsize = 8.5)
plt.show()
