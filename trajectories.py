import matplotlib
import matplotlib.pyplot as plt 
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import os
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 12

save_dir = "/home/pablo/ws/log/trajectories"

##########################################################
# WITH PREDICTION #
trajectories_pred = pd.read_csv(save_dir + "/trajectories_pred.csv")

# extract data from DataFrame
ardrone_x = trajectories_pred['aX'].tolist()
ardrone_y = trajectories_pred['aY'].tolist()
ardrone_z = trajectories_pred['aZ'].tolist()
summit_x = trajectories_pred['sX'].tolist()
summit_y = trajectories_pred['sY'].tolist()
summit_z = trajectories_pred['sZ'].tolist()

# 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(ardrone_x, ardrone_y, ardrone_z, 'r', label='UAV')
ax.plot(summit_x, summit_y, summit_z, 'g', label='UGV')
ax.set(xlabel='x (m)', ylabel='y (m)', zlabel='z (m)')
ax.legend()
fig.savefig(os.path.join(save_dir, "traj3D_pred.pdf"), format='pdf')
fig.savefig(os.path.join(save_dir, "traj3D_pred.png"), format='png')

# 2D
fig, ax = plt.subplots()
ax.plot(ardrone_x, ardrone_y, 'r', label='UAV')
ax.plot(summit_x, summit_y, 'g', label='UGV')
ax.set(xlabel='x (m)', ylabel='y (m)')
ax.legend()
ax.grid()
fig.savefig(os.path.join(save_dir, "traj2D_pred.pdf"), format='pdf')
fig.savefig(os.path.join(save_dir, "traj2D_pred.png"), format='png')

plt.show()


##########################################################
# WITHOUT PREDICTION #
trajectories_no_pred = pd.read_csv(save_dir + "/trajectories_NO_pred.csv")

# extract data from DataFrame
ardrone_x = trajectories_no_pred['aX'].tolist()
ardrone_y = trajectories_no_pred['aY'].tolist()
ardrone_z = trajectories_no_pred['aZ'].tolist()
summit_x = trajectories_no_pred['sX'].tolist()
summit_y = trajectories_no_pred['sY'].tolist()
summit_z = trajectories_no_pred['sZ'].tolist()

# 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(ardrone_x, ardrone_y, ardrone_z, 'r', label='UAV')
ax.plot(summit_x, summit_y, summit_z, 'g', label='UGV')
ax.set(xlabel='x (m)', ylabel='y (m)', zlabel='z (m)')
ax.legend()
fig.savefig(os.path.join(save_dir, "traj3D_NO_pred.pdf"), format='pdf')
fig.savefig(os.path.join(save_dir, "traj3D_NO_pred.png"), format='png')

# 2D
fig, ax = plt.subplots()
ax.plot(ardrone_x, ardrone_y, 'r', label='UAV')
ax.plot(summit_x, summit_y, 'g', label='UGV')
ax.set(xlabel='x (m)', ylabel='y (m)')
ax.legend()
ax.grid()
fig.savefig(os.path.join(save_dir, "traj2D_NO_pred.pdf"), format='pdf')
fig.savefig(os.path.join(save_dir, "traj2D_NO_pred.png"), format='png')


plt.show()