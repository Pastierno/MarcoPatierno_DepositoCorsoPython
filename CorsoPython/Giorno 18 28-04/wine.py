from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

data = load_wine()
X = data.data
y = data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
X_train_no_scaler, X_test_no_scaler, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf_no_scaler = DecisionTreeClassifier(random_state=42)

clf.fit(X_train, y_train)
clf_no_scaler.fit(X_train_no_scaler, y_train)

y_pred = clf.predict(X_test)
y_pred_no_scaler = clf_no_scaler.predict(X_test_no_scaler)


print("Accuratezza senza scaler:", accuracy_score(y_test, y_pred_no_scaler))
print("Report senza scaler:\n", classification_report(y_test, y_pred_no_scaler))
print("Confusione senza scaler:\n", confusion_matrix(y_test, y_pred_no_scaler))

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

print(data.DESCR)

# Nuova predict
wine1 = [[13.5, 2.5, 2.0, 20.0, 100.0, 2.5, 2.0, 0.5, 1.0, 3.0, 1.0, 3.0, 800]]

y_pred1 = clf.predict(scaler.transform(wine1))

print("Predizione:", y_pred1)
