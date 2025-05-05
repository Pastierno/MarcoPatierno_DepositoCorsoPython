import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PowerTransformer, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from catboost import CatBoostRegressor

# 1. Carica i dati (modifica il percorso se necessario)
df = pd.read_csv(r'C:\Users\fabri\Desktop\MarcoPatierno_DepositoCorsoPython\env\Giorno 21 05-05\esercitazione\data\cause_of_deaths.csv')

# 2. Metti in formato long e pulisci
df_long = (
    df.melt(id_vars=['Country/Territory', 'Year'], var_name='Disease', value_name='Probability')
    .rename(columns={'Country/Territory': 'Country'})
)
df_long['Probability'] = (
    df_long['Probability'].astype(str)
    .str.replace(r"[^0-9.]", "", regex=True)
    .astype(float)
)

# 3. Definisci feature X e target y
y = df_long['Probability'] / 100  # da percentuale a frazione
X = df_long[['Country', 'Year', 'Disease']]

# 4. Suddividi in train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Preprocessing per Year (numerico)
preprocessor = ColumnTransformer([
    ('num', Pipeline([
        ('pt', PowerTransformer(method='yeo-johnson')),
        ('sc', StandardScaler())
    ]), ['Year'])
], remainder='passthrough')  # Country e Disease passano inalterate

# 6. Modello che gestisce categorie: CatBoost
#    In output di preprocessor, colonne: [Year_transformed, Country, Disease]
#    Quindi cat_features=[1,2]
model = CatBoostRegressor(random_state=42, verbose=0, cat_features=[1, 2])

pipeline = Pipeline([
    ('prep', preprocessor),
    ('model', model)
])

# 7. Addestra e valuta
pipeline.fit(X_train, y_train)
print(f"R² sul test set: {pipeline.score(X_test, y_test):.3f}")

# 8. Funzione di predizione per il menu
def predict_probability(country: str, year: int, disease: str) -> float:
    sample = pd.DataFrame([{'Country': country, 'Year': year, 'Disease': disease}])
    raw = pipeline.predict(sample)[0]
    return round(raw * 100, 2)  # torna a percentuale

# Esempio di utilizzo
if __name__ == '__main__':
    print(predict_probability('Italy', 2020, 'Malaria'))