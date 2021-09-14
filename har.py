import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import itertools

def one_dim_plot(data):
  groups = data.groupby("label")
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
  groups = data.groupby("label")
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
  groups = data.groupby("label")
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

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.figure(figsize=(10,10))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()