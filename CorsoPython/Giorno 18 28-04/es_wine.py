import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# dataset Wine
data = load_wine()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

# esplorazione del dataset
print("Numero di campioni per classe:")
print(y.value_counts())
print("\nStatistiche di base delle feature:")
print(X.describe())

# visualizzazione
plt.figure()
classes = y.value_counts().sort_index()
plt.bar(data.target_names, classes)
plt.title("Distribuzione delle classi")
plt.xlabel("Classe")
plt.ylabel("Numero di campioni")
plt.show()

# riduzione dimensionale con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
plt.figure()
for cls in np.unique(y):
    idx = y == cls
    plt.scatter(X_pca[idx, 0], X_pca[idx, 1], label=data.target_names[cls])
plt.title("PCA - 2 componenti principali")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend()
plt.show()

#suddivisione in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# valutazione delle performance
y_pred = rf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision (macro):", precision_score(y_test, y_pred, average='macro'))
print("Recall (macro):", recall_score(y_test, y_pred, average='macro'))
print("F1-score (macro):", f1_score(y_test, y_pred, average='macro'))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=data.target_names))

# importanza delle feature
importances = pd.Series(rf.feature_importances_, index=data.feature_names).sort_values(ascending=False)
plt.figure()
plt.bar(importances.index, importances)
plt.title("Importanza delle feature")
plt.xticks(rotation=90)
plt.ylabel("Importanza")
plt.show()

# matrice di confusione
cm = confusion_matrix(y_test, y_pred)
plt.figure()
plt.imshow(cm, cmap='Blues')
plt.title("Matrice di confusione")
plt.xlabel("Predetto")
plt.ylabel("Reale")
plt.colorbar()
plt.xticks(np.arange(len(data.target_names)), data.target_names, rotation=45)
plt.yticks(np.arange(len(data.target_names)), data.target_names)
plt.show()

# ottimizzazione dei parametri con GridSearchCV
param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 10]}
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid.fit(X_train, y_train)
print("Best parameters:", grid.best_params_)

# valutazione del modello ottimizzato
best_rf = grid.best_estimator_
y_pred_best = best_rf.predict(X_test)
print("\nPerformance con modello ottimizzato:")
print("Accuracy:", accuracy_score(y_test, y_pred_best))
print("Precision (macro):", precision_score(y_test, y_pred_best, average='macro'))
print("Recall (macro):", recall_score(y_test, y_pred_best, average='macro'))
print("F1-score (macro):", f1_score(y_test, y_pred_best, average='macro'))
print("\nClassification Report modello ottimizzato:\n", classification_report(y_test, y_pred_best, target_names=data.target_names))
