# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:26:29 2020

@author: ariel
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
iris_dataset = load_iris()
#%% K nearest neighbors
score_knn = []

for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'])
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)
    score_knn.append(knn.score(X_test, y_test))

promedio_scoreKNN = sum(score_knn)/len(score_knn)
print(f'El promedio del score de KNN es: {promedio_scoreKNN:.2f}')
#%% Árboles de decisión
score_arboles = []

for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'])
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    score_arboles.append(clf.score(X_test, y_test))

promedio_scoreArboles = sum(score_arboles)/len(score_arboles)
print(f'El promedio del score de Arboles de Decisión es: {promedio_scoreArboles:.2f}')
#%% Random Forest
score_random_forest = []
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'])
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    score_random_forest.append(clf.score(X_test, y_test))
promedio_score_random_forest = sum(score_random_forest)/len(score_random_forest)
print(f'El promedio del score de Random Forest es: {promedio_score_random_forest:.2f}')


















