import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\fabri\Desktop\MarcoPatierno_DepositoCorsoPython\env\Giorno 18 28-04\train (2).csv")
# print(df.head())
# print(df.isna().sum())
# print(df.shape)
print(df.describe())
df["Age"] = df["Age"].fillna(df["Age"].mean())

numeric_df = df.select_dtypes(include=['int64', 'float64'])


correlation_matrix = numeric_df.corr()

# Visualizza la matrice di correlazione
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matrice di Correlazione tra Variabili Numeriche')
plt.tight_layout()
#plt.show()

# Stampa la matrice di correlazione
print("Matrice di correlazione:")
print(correlation_matrix)

df = df.drop(columns=["Cabin", "PassengerId", "Ticket", "Name"])
df = df.dropna(subset=['Embarked'])
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

print(df.head())
print(df.isna().sum())

# Seleziona le colonne di input e output
X = df.drop(columns=["Survived"])
y = df["Survived"]

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inizializza il classificatore Random
rf = RandomForestClassifier(random_state=42)

rf.fit(X_train, y_train)

y_pred = rf.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 10]}
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid.fit(X_train, y_train)
print("Best parameters:", grid.best_params_)

best_rf = grid.best_estimator_
y_pred_best = best_rf.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred_best))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_best))
print("Classification Report:")
print(classification_report(y_test, y_pred_best))