from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# #Generiamo un dataset di esempio con parametri corretti
# X, y = make_classification(n_samples=100, n_features=2, 
#                            n_informative=2, n_redundant=0, 
#                            n_repeated=0, n_classes=2, random_state=42)

data = load_iris()
X = data.data
y = data.target
#Dividiamo in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Creiamo il modello Decision Tree
tree = DecisionTreeClassifier(max_depth=3, criterion="gini", random_state=42)
tree.fit(X_train, y_train)

#Visualizziamo l'albero decisionale
# plt.figure(figsize=(12, 6))
# plot_tree(tree, feature_names=data.feature_names, class_names=["Setosa", "Versicolor", "Virginica"], filled=True)
# plt.title("Decision Tree Classifier (Gini Impurity)")
# plt.show()

# Import GridSearchCV

# Define parameter grid
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy']
}

# Create a grid search object
grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,  # 5-fold cross-validation
    scoring='accuracy',
    n_jobs=-1,  # Use all available cores
    verbose=1
)

# Fit the grid search
grid_search.fit(X_train, y_train)

# Print best parameters and score
print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Score:", grid_search.best_score_)

# Get the best model
best_tree = grid_search.best_estimator_

# Evaluate on test set
y_pred = best_tree.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Setosa", "Versicolor", "Virginica"]))

# Visualize the best decision tree
plt.figure(figsize=(12, 6))
plot_tree(best_tree, feature_names=data.feature_names, class_names=["Setosa", "Versicolor", "Virginica"], filled=True)
plt.title("Best Decision Tree Classifier")
plt.show()