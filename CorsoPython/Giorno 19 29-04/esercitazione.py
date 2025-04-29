import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

df = pd.read_csv(r"C:\Users\fabri\Desktop\MarcoPatierno_DepositoCorsoPython\env\Giorno 18 28-04\train (2).csv")
# Pulizia
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.drop(columns=["Cabin", "PassengerId", "Ticket", "Name"])
df = df.dropna(subset=['Embarked'])
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1 
df['IsAlone'] = (df['FamilySize'] == 1).astype(int) 

print(df.head())

# Seleziona le colonne di input e output
X = df.drop(columns=["Survived"])
y = df["Survived"]

# Dividi in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scala i dati
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 1. DECISION TREE
print("\n" + "_"*50)
print("DECISION TREE CLASSIFIER")
print("_"*50)

# Definisci i parametri da testare
param_grid_dt = {
    'max_depth': [3, 5, 10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy']
}

# Crea il modello e il GridSearchCV
dt = DecisionTreeClassifier(random_state=42)
grid_search_dt = GridSearchCV(dt, param_grid_dt, cv=5, scoring='accuracy', n_jobs=-1)

# Addestra GridSearch
print("Ricerca dei migliori parametri per Decision Tree...")
grid_search_dt.fit(X_train_scaled, y_train)

# Mostra i migliori parametri
print(f"Migliori parametri trovati: {grid_search_dt.best_params_}")
print(f"Miglior punteggio di validazione: {grid_search_dt.best_score_:.4f}")

# Addestra il modello finale con i migliori parametri
best_dt = grid_search_dt.best_estimator_
best_dt.fit(X_train_scaled, y_train)

# Valutazione
y_pred_dt = best_dt.predict(X_test_scaled)
accuracy_dt = accuracy_score(y_test, y_pred_dt)

print("\nValutazione del modello Decision Tree:")
print(f"Accuracy: {accuracy_dt:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_dt))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_dt))

# 2. RANDOM FOREST
print("\n" + "_"*50)
print("RANDOM FOREST CLASSIFIER")
print("_"*50)

# Definisci i parametri da testare
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# Crea il modello e il GridSearchCV
rf = RandomForestClassifier(random_state=42)
grid_search_rf = GridSearchCV(rf, param_grid_rf, cv=5, scoring='accuracy', n_jobs=-1)

# Addestra GridSearch
print("Ricerca dei migliori parametri per Random Forest...")
grid_search_rf.fit(X_train_scaled, y_train)

# Mostra i migliori parametri
print(f"Migliori parametri trovati: {grid_search_rf.best_params_}")
print(f"Miglior punteggio di validazione: {grid_search_rf.best_score_:.4f}")

# Addestra il modello finale con i migliori parametri
best_rf = grid_search_rf.best_estimator_
best_rf.fit(X_train_scaled, y_train)

# Valutazione
y_pred_rf = best_rf.predict(X_test_scaled)
accuracy_rf = accuracy_score(y_test, y_pred_rf)

print("\nValutazione del modello Random Forest:")
print(f"Accuracy: {accuracy_rf:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_rf))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

# Confronto tra i modelli
print("\n" + "_"*50)
print("CONFRONTO TRA I MODELLI")
print("_"*50)
print(f"Decision Tree Accuracy: {accuracy_dt:.4f}")
print(f"Random Forest Accuracy: {accuracy_rf:.4f}")
print(f"Differenza: {abs(accuracy_rf - accuracy_dt):.4f}")

# Feature importance per il miglior modello
# if accuracy_rf >= accuracy_dt:
#     feature_importance = pd.DataFrame({
#         'Feature': X.columns,
#         'Importance': best_rf.feature_importances_
#     }).sort_values('Importance', ascending=False)
    
#     print("\nImportanza delle feature (Random Forest):")
#     print(feature_importance)
# else:
#     feature_importance = pd.DataFrame({
#         'Feature': X.columns,
#         'Importance': best_dt.feature_importances_
#     }).sort_values('Importance', ascending=False)
    
#     print("\nImportanza delle feature (Decision Tree):")
#     print(feature_importance)

#xgboost
print("\n" + "_"*50)
print("XGBOOST CLASSIFIER")
print("_"*50)

# Definisci i parametri da testare
param_grid_xgb = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

# Crea il modello e il GridSearchCV
xgb = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
grid_search_xgb = GridSearchCV(xgb, param_grid_xgb, cv=5, scoring='accuracy', n_jobs=-1)

# Addestra GridSearch
print("Ricerca dei migliori parametri per XGBoost...")
grid_search_xgb.fit(X_train_scaled, y_train)

# Mostra i migliori parametri
print(f"Migliori parametri trovati: {grid_search_xgb.best_params_}")
print(f"Miglior punteggio di validazione: {grid_search_xgb.best_score_:.4f}")

# Addestra il modello finale con i migliori parametri
best_xgb = grid_search_xgb.best_estimator_
best_xgb.fit(X_train_scaled, y_train)

# Valutazione
y_pred_xgb = best_xgb.predict(X_test_scaled)
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)

print("\nValutazione del modello XGBoost:")
print(f"Accuracy: {accuracy_xgb:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_xgb))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_xgb))

# Confronto tra i modelli aggiornato
print("\n" + "_"*50)
print("CONFRONTO TRA I MODELLI AGGIORNATO")
print("_"*50)
print(f"Decision Tree Accuracy: {accuracy_dt:.4f}")
print(f"Random Forest Accuracy: {accuracy_rf:.4f}")
print(f"XGBoost Accuracy: {accuracy_xgb:.4f}")
print(f"Differenza massima: {max(abs(accuracy_rf - accuracy_dt), abs(accuracy_xgb - accuracy_rf), abs(accuracy_xgb - accuracy_dt)):.4f}")