import scipy
import scipy.spatial
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import pandas as pd

#pass the distance matrix
clus20 = pd.read_csv(r"/Users/manish/Documents/UniversityofMissouri/Spring2017/Spatial/Homeworks/HW1/HW1_Submission/eudist.csv", sep = ",")
Y20 = scipy.spatial.distance.pdist(clus20[clus20.columns[1:9]], 'cosine')
A = pd.DataFrame(scipy.spatial.distance.squareform(Y20))
mask =  np.tri(A.shape[0], k=-1)
A = np.ma.array(A, mask=mask.T) #Mask upper triangle

sns.set_context({"figure.figsize": (12, 12)})
sns.set_style("white")

fig = plt.figure()
ax1 = fig.add_subplot(111)
cmap = cm.get_cmap('Blues', 20)
cmap.set_bad('w') # default value is 'k'
ax1.imshow(A, cmap=cmap )
plt.ylabel("Cluster", size = 1)
plt.xlabel("Cluster", size = 1)
sns.despine()
plt.colorbar(ax1.matshow(A, cmap=cmap, vmin=0, vmax=1), shrink=.75)

ax1.xaxis.set_label_position('bottom')
ax1.xaxis.set_ticks_position('bottom')
plt.xticks(range(0,10,1), size = 1)
plt.yticks(range(0,10,1), size = 1)

#generate the graphs
plt.show()
#plt.savefig(r'C:\cosine_similarity.jpg', dpi=220, bbox_inches='tight')
