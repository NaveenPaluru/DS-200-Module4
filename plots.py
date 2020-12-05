#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:18:16 2020

@author: Naveen Paluru
"""

"""

TASK 

Select datasets from https://data.gov.in/ and create (a) a scatter plot, (b) a box plot,and 
(c)  a  bar  or  line  plot  from  them  using  mathplotlib  library. Upload all the  plots
and the Python scripts you wrote to this repository as a single zip file, and also include 
Readme.md documentation for the same listing the data sources and the observations from the 
plots,including citations. Use the git or svncommand line clients to perform the operations.

"""

"""
The case study is of Percentage of Schools with Computers from 2013-14 to 2015-16 in India.
The details (data in %) are available year wise, state wise and also Overall (across India).
"""

"""
Sample Data
                      State_UT     year  All Schools
                      
0    Andaman & Nicobar Islands  2013-14        53.06
1    Andaman & Nicobar Islands  2014-15        57.25
2    Andaman & Nicobar Islands  2015-16        57.00
3               Andhra Pradesh  2013-14        29.57
4               Andhra Pradesh  2014-15        28.06
..                         ...      ...          ...

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the exel file
df = pd.read_excel (r'./datafile.xls')

# Extract the last column
df1 = df.iloc[:, 12]

# Convert the data to numpy array
gg=df1.to_numpy()


#%% Bar Plots

# Get the overall results and make bar plot
hh = gg[[107,108,109]]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
years = ['2013-14', '2014-15 ', '2015-16']
data = hh
ax.bar(years,data,width = 0.35)
#ax.set_ylabel('Percentage of Schools with Computer')
plt.ylabel('Percentage of Schools with Computer', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=18)
plt.show()

#%% Box Plots

# get year wise details and lot the box plot

# remove Telanga's data as it has only two years data

kk = np.ones(110).astype(np.bool).reshape(110,)
kk[93] = 0
kk[94] = 0
gg1 = gg[kk]

# 2013-14 data
hh1 = gg1[0:105:3]; spread1 = np.std(hh1)
center1     = np.mean(hh1)
flier_high1 = np.max(hh1)
flier_low1  = np.min(hh1)
data1 = np.asarray([spread1, center1, flier_high1, flier_low1])

# 2014-15 data
hh2 = gg1[1:105:3]; spread2 = np.std(hh2)
center2     = np.mean(hh2)
flier_high2 = np.max(hh2)
flier_low2  = np.min(hh2)
data2 = np.asarray([spread2, center2, flier_high2, flier_low2])

# 2015-16 data
hh3 = gg1[2:105:3]; spread3 = np.std(hh3)
center3     = np.mean(hh3)
flier_high3 = np.max(hh3)
flier_low3  = np.min(hh3)
data3 = np.asarray([spread3, center3, flier_high3, flier_low3])

fig1, ax1 = plt.subplots()
ax1.boxplot([data1, data2, data3])
plt.xticks([1, 2, 3], ['2013-14','2014-15', '2014-16'])
plt.ylabel('% of the Schools with Computers \n across states in India', fontsize=16)
ax1.tick_params(axis='both', which='major', labelsize=18)


#%% Scatter Plots

labels =  df.iloc[:, 0]
labels = labels[0:110:3]
labels = labels[0:36]
labels = list(labels)
fig, ax = plt.subplots()
phi = np.linspace(0, 2*np.pi, 60)

rgb_cycle = np.vstack((            # Three sinusoids
    .5*(1.+np.cos(phi          )), # scaled to [0,1]
    .5*(1.+np.cos(phi+2*np.pi/3)), # 120° phase shifted.
    .5*(1.+np.cos(phi-2*np.pi/3)))).T # Shape = (60,3)
        
clrs = rgb_cycle[0:35,:]

for i in range(2, 34, 6):
    ax.scatter(hh2[i],hh3[i],c=clrs[i,:],label = labels[i])
    
plt.ylabel(' % of Schools with Computer \n (2015-16)', fontsize=16)
plt.xlabel(' % of Schools with Computer (2014-15)', fontsize=16)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
          fancybox=True, shadow=True, ncol=3)
ax.grid(True)









