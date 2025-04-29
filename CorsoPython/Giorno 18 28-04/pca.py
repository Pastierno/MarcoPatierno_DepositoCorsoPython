import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.random.rand(200, 5)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

n_comp = 2
pca = PCA(n_components=n_comp)

X_pca = pca.fit_transform(X_scaled)

print("Varianza spiegata da ciascun componente: ", pca.explained_variance_ratio_)

plt.figure(figsize = (8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c="blue", edgecolor = "k", alpha = 0.7)
plt.xlabel("Prima componente principale")
plt.ylabel("Seconda componente principale")
plt.title("Visualizzazione dati dopo PCA (2D)")
plt.show()