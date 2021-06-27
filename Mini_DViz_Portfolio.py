'''

author: MahmoudSuliman


'''
# =============================================================================
# Importing libraries

import os
os.chdir(r'working directory')
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np

# =============================================================================
# =============================================================================
# Initial Inputs and values

# Spine positions to be removed
sp='right','left','top','bottom'

# x-axis grid indices
xgrid=np.repeat([0,1,2,3],4)

# y-axis grid indices
ygrid=np.array([3,2,1,0])
for i in range(1,3):
    ygrid=np.concatenate([ygrid,ygrid])

# Figure numbers
fignum= ['a1','a2','a3','a4', 'b1', 'b2', 'b3','b4',
         'c1','c2','c3','c4','d1','d2','d3','d4']

# Figure descriptions
descriptions= ['Different model calibration options vs. model efficiency',
         'Gantt Chart for measurement durations of different data types',
         'Average historical monthly hydroclimatic observations (10+ years)',
         'Catchment Budyko plot using different PET estimations',
         'Model efficiency for 1 Million Monte carlo simulations',
         'Estimated phase and water level change in a SAR interferograms',
         'Cross-sectional Elevation profile of Groundwater layers',
         'Groundwater particle travel time from a pollution zone to a lake',
         'Observed vs. predicted runoff from a rainfall-runoff model',
         'Wetland extent change based on water management options',
         'Regulation compliance of hypothetical water management options',
         'Estimated revenue based on different water management options',
         'Modeled results for minimized cost based on pollutant reduction',
         'Estimated remediation measure efficiency  vs. minimized costs',
         'The sensitivity of different modeled parameters (3d surface)',
         'Probability of pollutant remediation vs stochastic assumptions']

# defining text annotation function

def annotate(h,y,t,s):
    return x.text(h, y, t, fontsize=s, color='steelblue')

# =============================================================================
# =============================================================================
# Plotting

# plotting main grid and background
fig, axs = plt.subplots(4,4, figsize=(25,20), facecolor='aliceblue')
         
# loading the portfolio
for i in range(1,17):
    x=axs[ygrid[i-1],xgrid[i-1]]
    x.imshow(img.imread(str(i)+'.jpg')); x.set_xticks([]); x.set_yticks([])
    x.set_anchor('C') 

# Drawing the main frame
frame = plt.Rectangle((0.09, 0.09), 0.85, 0.85, fill=False, color="steelblue", 
                      lw=5, zorder=1000, transform=fig.transFigure, figure=fig)
fig.patches.extend([frame])

# Drawing x-grid using smaller arrows
for i in [580,1200,1850]:
    x=axs[0,0]
    x.arrow(-230,i,3400,0,clip_on=False, lw=2,head_width=0, head_length=0,
            ls=(0,(5,10)),fc='lightskyblue',ec='lightskyblue')

# Drawing y-grid using smaller arrows
for i in [680,1480,2320]:
    x=axs[0,0]
    x.arrow(i,-160,0,2650,clip_on=False, lw=2,head_width=0, head_length=0,
            ls=(0,(5,10)),fc='lightskyblue',ec='lightskyblue')


# Adding title
annotate(800, -300, 'My Portfolio', 100)

# create figure padding
for i,j in [3500,-400], [-600,-450], [800,4500]:
    annotate(i,j,' ', 80)

# drawing figure numbers on the main grid
# x-axis
for i,k in [200,'a'], [1100,'b'], [1850,'c'],[2700,'d']:
    annotate(i,2800,k, 80)

# y-axis
for j,k in [2250,'1'], [1550,'2'], [900,'3'],[200,'4']:
    annotate(-500,j,k, 80)


# Drawing the description box
frame = plt.Rectangle((0.12, -0.45), 0.8, 0.28, fill=False, color="steelblue", 
                      lw=3, ls='--',zorder=1000, transform=fig.transFigure, figure=fig)

fig.patches.extend([frame])

# Adding description box title
annotate(950, 3250, 'Description', 60)

# adding figure descriptions
pos=np.arange(3500,4350,100);pos
for i in range(0,8):
    annotate(0, pos[i], fignum[i]+') '+descriptions[i], 18)

for i in range(0,8):
    annotate(0+1600, pos[i], fignum[i+8]+') '+descriptions[i+8], 18)

# Saving the Portfolio
plt.savefig('Visualization_Progress_fin.jpg', dpi=300, bbox_inches='tight')

# =============================================================================
