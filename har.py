import matplotlib.pyplot as plt
import numpy as np

def one_dim_plot(data):
  groups = curr_data.groupby("label")
  #plt.figure(figsize=(10,1))
  fig = plt.figure(figsize=(10,1))
  ax = fig.add_subplot(111)
  colors = ['cornflowerblue', 'sandybrown']
  num = 0
  for name, group in groups:
    ax.scatter(group["userAcceleration.x_mean"][:100], np.zeros_like(group['userAcceleration.x_mean'][:100]), label=name, color=colors[num])
    plt.yticks([])
    num += 1
  plt.legend()
  plt.xlabel("Acceleration x gennemsnit")
  #plt.title("1D plot", fontsize=20)
  ax.set_title('1D scatterplot', fontsize=20)
  #fig.savefig('/content/gdrive/My Drive/studenterprojekt/fysioterapeuter/billeder/1d.png'.format(name), bbox_inches='tight')

def two_dim_plot(data):
  groups = curr_data.groupby("label")
  #plt.figure(figsize=(10,10))
  fig = plt.figure(figsize=(10,10))
  ax = fig.add_subplot(111)
  colors = ['cornflowerblue', 'sandybrown']
  num = 0
  for name, group in groups:
    plt.plot(group["userAcceleration.x_mean"][:100], group['userAcceleration.y_mean'][:100], marker="o", linestyle="", label=name, color=colors[num])
    num += 1
  #ax.Circle( (0.6, 0.6 ),0.3 ,fill = False )
  plt.legend()
  plt.xlabel("Acceleration x gennemsnit")
  plt.ylabel("Acceleration y gennemsnit")
  #plt.title("2D scatterplot", fontsize=20)
  ax.set_title('2D scatterplot', fontsize=20)
  #fig.savefig('/content/gdrive/My Drive/studenterprojekt/fysioterapeuter/billeder/2d_dot.png'.format(name), bbox_inches='tight')

def three_dim_plot(data):
  groups = curr_data.groupby("label")
  plt.figure(figsize=(10,10))
  fig = plt.figure(figsize=(10,10))
  ax = fig.add_subplot(111, projection='3d')
  colors = ['cornflowerblue', 'sandybrown']
  num = 0
  for name, group in groups:
    ax.scatter(group['userAcceleration.x_mean'][:100], group['userAcceleration.y_mean'][:100], group['userAcceleration.z_mean'][:100], label=name, color=colors[num])
    num += 1
  plt.legend()
  plt.xlabel("Acceleration x gennemsnit")
  plt.ylabel("Acceleration y gennemsnit")
  ax.set_zlabel("Acceleration z gennemsnit")
  ax.set_title('3D scatterplot', fontsize=20)
  #fig.savefig('/content/gdrive/My Drive/studenterprojekt/fysioterapeuter/billeder/3d.png'.format(name), bbox_inches='tight')