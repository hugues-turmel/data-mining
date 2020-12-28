# -*- coding: utf-8 -*-
"""TP_SVM_BASIC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1usleHLKNIPAqQfNCW78EAZA6YYsCNwaE
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

X = np.c_[(.4, -.7),
(-1.5, -1),
(-1.4, -.9),
(-1.3, -1.2),
(-1.1, -.2),
(-1.2, -.4),
(-.5, 1.2),
(-1.5, 2.1),
(1, 1),
(1.3, .8),
(1.2, .5),
(.2, -2),
(.5, -2.4),
(.2, -2.3),
(0, -2.7),
(1.3, 2.1)].T
Y = [0] * 8 + [1] * 8


for kernel in ('linear', 'poly', 'rbf'):
  clf = svm.SVC(kernel=kernel, gamma=1)
  clf.fit(X, Y)
fignum = 1
plt.figure(fignum, figsize=(4, 3))
plt.clf()
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none', zorder=10, edgecolors='k')
plt.scatter(X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.cm.Paired,edgecolors='k')
plt.axis('tight')
x_min = -3
x_max = 3
y_min = -3
y_max = 3
XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
fignum = fignum + 1
Z = Z.reshape(XX.shape)
plt.figure(fignum, figsize=(4, 3))
plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
plt.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'], levels=[-.5, 0, .5])
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
fignum = fignum + 1

g = [0.1, 0.2, 0.5, 1, 2, 3, 5, 10]
fignum = 1
plt.figure(figsize=(10,9))
for value in g:
  for kernel in ('linear', 'poly', 'rbf'):
    clf = svm.SVC(kernel=kernel, gamma=value)
    clf.fit(X, Y)
  x_min = -3
  x_max = 3
  y_min = -3
  y_max = 3
  XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
  Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
  Z = Z.reshape(XX.shape)
  plt.subplot(4,2,fignum)
  plt.title("gamma = {}".format(value))
  plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
  plt.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'], levels=[-.5, 0, .5])
  plt.xlim(x_min, x_max)
  plt.ylim(y_min, y_max)
  plt.xticks(())
  plt.yticks(())
  fignum = fignum + 1
plt.show()