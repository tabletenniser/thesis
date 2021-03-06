# coding: utf-8
# import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import pylab as pl
from PIL import Image
import numpy as np

from os import listdir
from os.path import isdir
from os.path import join
digits_new = {}
data = []
target = []
container_path = 'training_set'
folders = [f for f in sorted(listdir(container_path)) if isdir(join(container_path, f))]
#print folders
for folder in folders:
    folder_path = join(container_path, folder)
    #print folder
    documents = [join(folder_path, d) for d in sorted(listdir(folder_path))]
    for pic in documents:
        if not pic.endswith('png'):
            continue
        pil_im = Image.open(pic, 'r')
        data.append(np.asarray(pil_im).ravel())
        target.append(int(folder))
digits_new['data']=data
digits_new['target']=target
#print digits_new

from sklearn import svm
clf = svm.SVC()
#clf.fit(digits.data[:-1], digits.target[:-1])
clf.fit(digits_new['data'][:-5], digits_new['target'][:-5])
#print digits_new['data'][-1].reshape(24,24)
print 'svm predict:', clf.predict(digits_new['data'][-4])

# In[129]:

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(digits_new['data'][:-5], digits_new['target'][:-5])
# plt.imshow(digits_new['data'][-2].reshape(24,24))
# plt.show()
print 'knn predict:', int(neigh.predict(digits_new['data'][-2]))
print 'knn predict:', neigh.predict_proba(digits_new['data'][-2])

# In[128]:

pil_im = Image.open('training_set/test.png', 'r').convert('L')
# plt.imshow(np.asarray(pil_im))
# plt.show()
print 'test.png knn:', neigh.predict(np.asarray(pil_im).ravel())
print 'test.png knn:', neigh.predict_proba(np.asarray(pil_im).ravel())

