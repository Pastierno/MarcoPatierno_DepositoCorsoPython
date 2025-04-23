import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import os
import warnings
warnings.filterwarnings('ignore')  # Ignora warning per una visualizzazione più pulita

# Funzione per caricare i dati
def load_data(file_path):
    try:
        # Verifica se il file esiste
        if not os.path.exists(file_path):
            print(f"Errore: Il file {file_path} non esiste")
            # Prova a cercare il file nella directory corrente
            base_name = os.path.basename(file_path)
            if os.path.exists(base_name):
                file_path = base_name
                print(f"Trovato il file nella directory corrente: {base_name}")
            else:
                return None
                
        df = pd.read_csv(file_path)
        print(f"Dati caricati con successo: {len(df)} righe")
        
        # Verifica colonne essenziali
        required_cols = ['ETA', 'TARIFFA_MENSILE', 'DATI_CONSUMATI']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            print(f"Attenzione: Mancano le seguenti colonne: {missing_cols}")
        
        return df
    except Exception as e:
        print(f"Errore nel caricamento dei dati: {e}")
        return None

# Funzione per visualizzare i dati
def display_data(df, rows=5):
    if df is not None:
        print(f"\nPrime {rows} righe del dataset:")
        print(df.head(rows))
        print("\nColonne presenti nel dataset:")
        for idx, col in enumerate(df.columns, 1):
            print(f"{idx}. {col}")
        
        # Mostra dimensioni del dataframe
        print(f"\nDimensioni del dataset: {df.shape[0]} righe, {df.shape[1]} colonne")
    else:
        print("Nessun dato caricato")

# Funzione per analisi descrittiva
def descriptive_analysis(df):
    if df is not None:
        print("\nStatistiche descrittive:")
        pd.set_option('display.max_columns', None)  # Mostra tutte le colonne
        print(df.describe())
        pd.reset_option('display.max_columns')
        
        print("\nInformazioni sul dataset:")
        df.info()
        
        # Conteggio valori nulli
        null_counts = df.isnull().sum()
        if null_counts.sum() > 0:
            print("\nValori nulli nel dataset:")
            print(null_counts[null_counts > 0])
        
        print("\nConteggio dei valori:")
        for col in df.select_dtypes(include=['object', 'category']).columns:
            print(f"\nDistribuzione di {col}:")
            value_counts = df[col].value_counts()
            print(value_counts)
            
            # Visualizzazione per colonne categoriche con pochi valori unici
            if len(value_counts) <= 10:
                plt.figure(figsize=(10, 6))
                sns.countplot(y=col, data=df, order=value_counts.index)
                plt.title(f'Distribuzione di {col}')
                plt.tight_layout()
                plt.show()
    else:
        print("Nessun dato caricato")

# Funzione per pulizia dati
def clean_data(df):
    if df is not None:
        # Crea una copia per non modificare l'originale
        df_cleaned = df.copy()
        
        # Verifica età prima della pulizia
        print("\nRange età prima della pulizia:")
        print(f"Min: {df_cleaned['ETA'].min()}, Max: {df_cleaned['ETA'].max()}")
        
        # Filtra età tra 18 e 80 anni
        df_cleaned = df_cleaned[(df_cleaned['ETA'] >= 18) & (df_cleaned['ETA'] <= 80)]
        
        # Gestione valori nulli
        null_counts = df_cleaned.isnull().sum()
        if null_counts.sum() > 0:
            print("\nSostituzione dei valori nulli:")
            for col in df_cleaned.columns:
                if df_cleaned[col].isnull().sum() > 0:
                    if df_cleaned[col].dtype.kind in 'ifc':  # Numerico
                        value = df_cleaned[col].median()
                        df_cleaned[col].fillna(value, inplace=True)
                        print(f"- {col}: sostituiti con mediana ({value})")
                    else:  # Categorico/testo
                        value = df_cleaned[col].mode()[0]
                        df_cleaned[col].fillna(value, inplace=True)
                        print(f"- {col}: sostituiti con moda ({value})")
        
        # Gestione outlier
        numeric_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_cols:
            if col != 'ETA':  # Età già filtrata sopra
                Q1 = df_cleaned[col].quantile(0.25)
                Q3 = df_cleaned[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                outliers = ((df_cleaned[col] < lower_bound) | (df_cleaned[col] > upper_bound)).sum()
                if outliers > 0:
                    print(f"\nOutlier in {col}: {outliers} righe")
                    print(f"Range valido: {lower_bound:.2f} - {upper_bound:.2f}")
                    
                    # Opzione: rimuovere o limitare gli outlier
                    if col in ['TARIFFA_MENSILE', 'DATI_CONSUMATI']:
                        old_count = len(df_cleaned)
                        df_cleaned = df_cleaned[(df_cleaned[col] >= lower_bound) & 
                                               (df_cleaned[col] <= upper_bound)]
                        print(f"Rimosse {old_count - len(df_cleaned)} righe con outlier in {col}")
        
        print("\nRange età dopo la pulizia:")
        print(f"Min: {df_cleaned['ETA'].min()}, Max: {df_cleaned['ETA'].max()}")
        print(f"Numero di righe rimanenti: {len(df_cleaned)}")
        
        return df_cleaned
    else:
        print("Nessun dato caricato")
        return None

# Funzione per creare nuove features
def create_features(df):
    if df is not None:
        # Crea una copia per non modificare l'originale
        df_featured = df.copy()
        
        # Costo per GB (gestendo divisione per zero)
        df_featured['COSTO_PER_GB'] = df_featured.apply(
            lambda row: row['TARIFFA_MENSILE'] / row['DATI_CONSUMATI'] 
            if row['DATI_CONSUMATI'] > 0 else np.nan, 
            axis=1
        )
        
        # Gestione valori NaN o infiniti nel costo per GB
        if df_featured['COSTO_PER_GB'].isna().sum() > 0:
            med_costo = df_featured['COSTO_PER_GB'].median()
            df_featured['COSTO_PER_GB'].fillna(med_costo, inplace=True)
            print(f"\nSostituiti {df_featured['COSTO_PER_GB'].isna().sum()} valori NaN in COSTO_PER_GB con la mediana ({med_costo:.2f})")
        
        # Categorizzazione per età
        df_featured['ETA_GRUPPO'] = pd.cut(
            df_featured['ETA'], 
            bins=[18, 30, 40, 50, 60, 70, 80], 
            labels=['18-30', '31-40', '41-50', '51-60', '61-70', '71-80']
        )
        
        # Utilizzo medio per gruppo età
        df_featured['UTILIZZO_MEDIO'] = df_featured.groupby('ETA_GRUPPO')['DATI_CONSUMATI'].transform('mean')
        
        # Categorizzazione consumo
        df_featured['CONSUMO_CATEGORIA'] = pd.qcut(
            df_featured['DATI_CONSUMATI'], 
            q=3, 
            labels=['Basso', 'Medio', 'Alto']
        )
        
        # Conversione colonna churn
        if 'CHURN' in df_featured.columns:
            # Gestisci vari formati possibili (0/1, SI/NO, True/False, ecc.)
            if df_featured['CHURN'].dtype == 'object':
                # Se è già una stringa, standardizza i valori
                df_featured['CHURN'] = df_featured['CHURN'].str.upper()
                df_featured['CHURN'] = df_featured['CHURN'].replace({'YES': 'SI', 'NO': 'NO', 'Y': 'SI', 'N': 'NO', 'TRUE': 'SI', 'FALSE': 'NO'})
            else:
                # Se è numerico, converti in SI/NO
                df_featured['CHURN'] = df_featured['CHURN'].replace({1: 'SI', 0: 'NO', True: 'SI', False: 'NO'})
        
        # Feature di fascia oraria per tariffa
        df_featured['TARIFFA_CATEGORIA'] = pd.qcut(
            df_featured['TARIFFA_MENSILE'], 
            q=3, 
            labels=['Economica', 'Media', 'Premium']
        )
        
        # Rapporto età/consumo
        df_featured['RAPPORTO_ETA_CONSUMO'] = df_featured['ETA'] / df_featured['DATI_CONSUMATI']
        # Gestione di possibili infiniti
        df_featured['RAPPORTO_ETA_CONSUMO'].replace([np.inf, -np.inf], np.nan, inplace=True)
        df_featured['RAPPORTO_ETA_CONSUMO'].fillna(df_featured['RAPPORTO_ETA_CONSUMO'].median(), inplace=True)
        
        print("\nNuove features create con successo:")
        print("- COSTO_PER_GB")
        print("- ETA_GRUPPO")
        print("- UTILIZZO_MEDIO")
        print("- CONSUMO_CATEGORIA")
        print("- TARIFFA_CATEGORIA")
        print("- RAPPORTO_ETA_CONSUMO")
        if 'CHURN' in df_featured.columns:
            print("- CHURN (standardizzata)")
        
        return df_featured
    else:
        print("Nessun dato caricato")
        return None

# Funzione per analisi delle correlazioni
def correlation_analysis(df):
    if df is not None:
        # Seleziona solo colonne numeriche
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        
        if len(numeric_cols) < 2:
            print("Insufficienti colonne numeriche per l'analisi di correlazione")
            return None
            
        # Calcola la matrice di correlazione
        correlation_matrix = df[numeric_cols].corr()
        
        print("\nMatrice di correlazione:")
        print(correlation_matrix.round(2))
        
        # Visualizzazione grafica con heatmap
        plt.figure(figsize=(10, 8))
        mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))  # Maschera triangolo superiore
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', mask=mask)
        plt.title('Matrice di Correlazione tra Variabili')
        plt.tight_layout()
        plt.show()
        
        # Evidenzia correlazioni significative
        threshold = 0.5
        high_correlations = []
        for i in range(len(correlation_matrix.columns)):
            for j in range(i):
                if abs(correlation_matrix.iloc[i, j]) > threshold:
                    high_correlations.append((correlation_matrix.columns[i], 
                                             correlation_matrix.columns[j], 
                                             correlation_matrix.iloc[i, j]))
        
        if high_correlations:
            print("\nCorrelazioni significative (|r| > 0.5):")
            for var1, var2, corr in high_correlations:
                print(f"- {var1} e {var2}: {corr:.2f}")
        
        return correlation_matrix
    else:
        print("Nessun dato caricato")
        return None

# Funzione per test ANOVA
def anova_test(df):
    if df is not None:
        if 'ETA_GRUPPO' not in df.columns:
            print("Colonna ETA_GRUPPO mancante. Esegui prima la creazione delle features.")
            return None
            
        # Crea gruppi per ANOVA
        groups = {}
        for group in df['ETA_GRUPPO'].unique():
            group_data = df[df['ETA_GRUPPO'] == group]['DATI_CONSUMATI']
            if len(group_data) > 0:  # Verifica che il gruppo abbia dati
                groups[group] = group_data
        
        if len(groups) < 2:
            print("Insufficienti gruppi per eseguire ANOVA (almeno 2 gruppi richiesti)")
            return None
            
        # Esegue test ANOVA
        try:
            # Converti in lista di array per f_oneway
            group_arrays = list(groups.values())
            f_stat, p_value = stats.f_oneway(*group_arrays)
            
            print("\nTest ANOVA - Confronto del consumo dati tra fasce d'età:")
            print(f"F-statistic: {f_stat:.4f}")
            print(f"p-value: {p_value:.4f}")
            
            if p_value < 0.05:
                print("Risultato: Ci sono differenze statisticamente significative tra i gruppi (p < 0.05)")
                
                # Se ANOVA è significativo, esegui test post-hoc per vedere quali gruppi differiscono
                print("\nTest post-hoc di Tukey per identificare differenze specifiche tra gruppi:")
                from statsmodels.stats.multicomp import pairwise_tukeyhsd
                
                # Prepara dati per Tukey test
                all_data = []
                all_groups = []
                for group, data in groups.items():
                    all_data.extend(data)
                    all_groups.extend([group] * len(data))
                
                # Esegui Tukey test
                tukey_results = pairwise_tukeyhsd(all_data, all_groups, alpha=0.05)
                print(tukey_results)
                
            else:
                print("Risultato: Non ci sono differenze statisticamente significative tra i gruppi (p >= 0.05)")
            
            # Visualizzazione grafica
            plt.figure(figsize=(12, 6))
            sns.boxplot(x='ETA_GRUPPO', y='DATI_CONSUMATI', data=df)
            plt.title('Distribuzione del Consumo Dati per Fascia d\'Età')
            plt.xlabel('Fascia d\'Età')
            plt.ylabel('Dati Consumati (GB)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            # Aggiunta: grafico di violino per visualizzare meglio la distribuzione
            plt.figure(figsize=(12, 6))
            sns.violinplot(x='ETA_GRUPPO', y='DATI_CONSUMATI', data=df)
            plt.title('Distribuzione del Consumo Dati per Fascia d\'Età (Violin Plot)')
            plt.xlabel('Fascia d\'Età')
            plt.ylabel('Dati Consumati (GB)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            
            return (f_stat, p_value)
        except Exception as e:
            print(f"Errore nell'esecuzione dell'ANOVA: {e}")
            return None
    else:
        print("Nessun dato caricato")
        return None

# Funzione per test chi-quadrato
def chi_square_test(df):
    if df is not None:
        if 'ETA_GRUPPO' not in df.columns or 'CONSUMO_CATEGORIA' not in df.columns:
            print("Colonne ETA_GRUPPO o CONSUMO_CATEGORIA mancanti. Esegui prima la creazione delle features.")
            return None
            
        # Crea tabella di contingenza
        contingency_table = pd.crosstab(df['ETA_GRUPPO'], df['CONSUMO_CATEGORIA'])
        
        # Verifica che ci siano abbastanza dati
        if contingency_table.size < 4:  # Almeno una tabella 2x2
            print("Dati insufficienti per il test chi-quadrato")
            return None
            
        # Verifica frequenze attese minime
        chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
        
        # Avviso se ci sono frequenze attese molto basse
        if (expected < 5).any():
            print("\nAttenzione: Alcune frequenze attese sono inferiori a 5, i risultati potrebbero essere inaffidabili.")
        
        print("\nTabella di contingenza tra Fasce d'Età e Categorie di Consumo:")
        print(contingency_table)
        
        # Aggiungiamo percentuali per riga per facilitare l'interpretazione
        print("\nPercentuali per riga (somma 100% per ogni fascia d'età):")
        row_percentages = contingency_table.div(contingency_table.sum(axis=1), axis=0) * 100
        print(row_percentages.round(1))
        
        # Test chi-quadrato
        print("\nTest Chi-Quadrato:")
        print(f"Chi²: {chi2:.4f}")
        print(f"p-value: {p:.4f}")
        print(f"Gradi di libertà: {dof}")
        
        # Interpretazione
        if p < 0.05:
            print("Risultato: Esiste un'associazione statisticamente significativa tra fascia d'età e categoria di consumo (p < 0.05)")
            
            # Aggiungiamo l'analisi dei residui standardizzati per individuare le celle che contribuiscono maggiormente
            observed = contingency_table.values
            row_sum = observed.sum(axis=1).reshape(-1, 1)
            col_sum = observed.sum(axis=0).reshape(1, -1)
            total = observed.sum()
            expected = np.outer(row_sum, col_sum) / total
            residuals = (observed - expected) / np.sqrt(expected)
            
            print("\nResidui standardizzati (>1.96 o <-1.96 sono significativi):")
            residuals_df = pd.DataFrame(residuals, index=contingency_table.index, columns=contingency_table.columns)
            print(residuals_df.round(2))
            
            # Identifica celle con residui significativi
            significant_cells = []
            for i, idx in enumerate(contingency_table.index):
                for j, col in enumerate(contingency_table.columns):
                    if abs(residuals[i, j]) > 1.96:
                        sign = "maggiore" if residuals[i, j] > 0 else "minore"
                        significant_cells.append(f"- Fascia {idx} con consumo {col}: {sign} del previsto (residuo: {residuals[i, j]:.2f})")
            
            if significant_cells:
                print("\nAssociazioni significative:")
                for cell in significant_cells:
                    print(cell)
        else:
            print("Risultato: Non esiste un'associazione statisticamente significativa tra fascia d'età e categoria di consumo (p >= 0.05)")
        
        # Visualizzazione grafica
        plt.figure(figsize=(12, 6))
        contingency_table.plot(kind='bar', stacked=True)
        plt.title('Distribuzione delle Categorie di Consumo per Fascia d\'Età')
        plt.xlabel('Fascia d\'Età')
        plt.ylabel('Conteggio')
        plt.legend(title='Categoria Consumo')
        plt.tight_layout()
        plt.show()
        
        # Grafico a mosaico per visualizzare meglio le proporzioni
        try:
            from statsmodels.graphics.mosaicplot import mosaic
            plt.figure(figsize=(12, 8))
            mosaic(df, ['ETA_GRUPPO', 'CONSUMO_CATEGORIA'], title='Grafico a Mosaico: Età vs Consumo')
            plt.tight_layout()
            plt.show()
        except:
            pass
        
        return (chi2, p, dof)
    else:
        print("Nessun dato caricato")
        return None

# Funzione per regressione logistica migliorata
def logistic_regression(df):
    if df is not None:
        if 'CHURN' not in df.columns:
            print("Colonna CHURN mancante nel dataset. Impossibile procedere con la regressione logistica.")
            return None
            
        # Verifica che ci siano valori per entrambe le classi
        churn_counts = df['CHURN'].value_counts()
        if len(churn_counts) < 2:
            print(f"Dati insufficienti: trovato solo '{churn_counts.index[0]}' nella colonna CHURN")
            return None
            
        # Prepara le variabili per la regressione
        print("\nSeleziona le feature da utilizzare per la regressione:")
        print("0. Utilizza tutte le feature numeriche")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        for i, col in enumerate(numeric_cols, 1):
            print(f"{i}. {col}")
            
        choice = input("\nInserisci i numeri delle feature da includere separati da virgola (0 per tutte): ")
        
        try:
            if choice == "0":
                selected_features = numeric_cols
            else:
                selected_indices = [int(idx.strip()) - 1 for idx in choice.split(",")]
                selected_features = [numeric_cols[idx] for idx in selected_indices]
                
            if not selected_features:
                print("Nessuna feature selezionata. Utilizzo tutte le feature numeriche.")
                selected_features = numeric_cols
                
            print(f"\nFeature selezionate: {', '.join(selected_features)}")
            
            X = df[selected_features]
            
            # Standardizza i dati
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
            
            # Verifica e converte la variabile target
            y = df['CHURN']
            if y.dtype == 'object':
                # Mappa i valori testuali a numeri
                value_map = {'SI': 1, 'NO': 0}
                y = y.map(value_map)
                
                # Verifica che ci siano entrambe le classi dopo la mappatura
                if len(y.unique()) < 2:
                    print("Errore: dopo la conversione, è presente una sola classe nella variabile target")
                    return None
            
            # Verifica valori mancanti
            if X_scaled.isnull().any().any() or y.isnull().any():
                print("Attenzione: rilevati valori mancanti. Imputazione...")
                imputer = SimpleImputer(strategy='median')
                X_scaled = pd.DataFrame(imputer.fit_transform(X_scaled), columns=X_scaled.columns)
                y = y.fillna(y.mode()[0])
            
            # Split dei dati con stratificazione per gestire classi sbilanciate
            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, y, test_size=0.3, random_state=42, stratify=y
            )
            
            # Controlla se i dati sono sbilanciati
            class_counts = y.value_counts()
            imbalance_ratio = class_counts.min() / class_counts.max()
            if imbalance_ratio < 0.3:
                print(f"\nAttenzione: classi sbilanciate (ratio: {imbalance_ratio:.2f})")
                print("Utilizzo di class_weight='balanced' per gestire lo sbilanciamento")
                class_weight = 'balanced'
            else:
                class_weight = None
                
            # Creazione e training del modello
            C_values = [0.01, 0.1, 1.0, 10.0]
            best_score = 0
            best_C = 1.0
            
            print("\nRicerca dell'iperparametro C ottimale...")
            for C in C_values:
                model = LogisticRegression(C=C, max_iter=2000, class_weight=class_weight)
                cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='roc_auc')
                avg_score = np.mean(cv_scores)
                print(f"C={C}: ROC AUC = {avg_score:.4f}")
                if avg_score > best_score:
                    best_score = avg_score
                    best_C = C
            
            print(f"\nUtilizzo del miglior valore C = {best_C}")
            model = LogisticRegression(C=best_C, max_iter=2000, class_weight=class_weight)
            model.fit(X_train, y_train)
            
            # Predizioni
            y_pred = model.predict(X_test)
            y_pred_prob = model.predict_proba(X_test)[:, 1]
            
            # Valutazione del modello
            accuracy = accuracy_score(y_test, y_pred)
            conf_matrix = confusion_matrix(y_test, y_pred)
            report = classification_report(y_test, y_pred)
            
            # Calcola ROC curve e AUC
            fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
            roc_auc = auc(fpr, tpr)
            
            print("\nModello di Regressione Logistica per Previsione Churn:")
            print(f"Accuratezza: {accuracy:.4f}")
            print(f"ROC AUC: {roc_auc:.4f}")
            
            print("\nMatrice di Confusione:")
            print(conf_matrix)
            
            print("\nReport di Classificazione:")
            print(report)
            
            # Importanza delle feature
            coefficients = pd.DataFrame(
                {'Feature': X.columns, 'Coefficient': model.coef_[0]}
            ).sort_values('Coefficient', ascending=False)
            
            print("\nImportanza delle Feature:")
            print(coefficients)
            
            # Visualizzazione
            plt.figure(figsize=(8, 6))
            sns.barplot(x='Coefficient', y='Feature', data=coefficients)
            plt.title('Importanza delle Feature nel Modello di Churn')
            plt.tight_layout()
            plt.show()
            
            # Grafico ROC
            plt.figure(figsize=(8, 6))
            plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
            plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('Tasso falsi positivi')
            plt.ylabel('Tasso veri positivi')
            plt.title('Curva ROC per predizione Churn')
            plt.legend(loc="lower right")
            plt.tight_layout()
            plt.show()
            
            return model
        except Exception as e:
            print(f"Errore nella regressione logistica: {e}")
            return None
    else:
        print("Nessun dato caricato")
        return None

# Funzione per clustering K-means migliorata
def clustering_kmeans(df):
    if df is not None:
        try:
            # Seleziona features per clustering
            print("\nSeleziona le feature da utilizzare per il clustering:")
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            
            # Rimuovi eventuali colonne di cluster esistenti
            if 'CLUSTER' in numeric_cols:
                numeric_cols.remove('CLUSTER')
                
            # Mostra le opzioni
            print("0. Utilizza feature raccomandate (ETA, DATI_CONSUMATI, TARIFFA_MENSILE)")
            for i, col in enumerate(numeric_cols, 1):
                print(f"{i}. {col}")
                
            choice = input("\nInserisci i numeri delle feature da includere separati da virgola (0 per raccomandate): ")
            
            if choice == "0":
                # Feature raccomandate
                selected_features = ['ETA', 'DATI_CONSUMATI', 'TARIFFA_MENSILE']
                # Verifica che esistano
                missing = [f for f in selected_features if f not in df.columns]
                if missing:
                    print(f"Features raccomandate mancanti: {missing}. Seleziona manualmente.")
                    return None
            else:
                # Features selezionate dall'utente
                selected_indices = [int(idx.strip()) - 1 for idx in choice.split(",")]
                selected_features = [numeric_cols[idx] for idx in selected_indices if 0 <= idx < len(numeric_cols)]
                
            if not selected_features:
                print("Nessuna feature valida selezionata.")
                return None
                
            print(f"\nFeature selezionate: {', '.join(selected_features)}")
            
            # Estrai i dati
            features = df[selected_features]
            
            # Gestisci valori mancanti
            if features.isnull().any().any():
                print("Imputazione dei valori mancanti...")
                imputer = SimpleImputer(strategy='median')
                features = pd.DataFrame(imputer.fit_transform(features), columns=features.columns)
            
            # Standardizzazione
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(features)
            
            # Determinazione del numero ottimale di cluster
            max_k = min(10, len(df) // 20)  # Limita k in base alla dimensione del dataset
            k_range = range(2, max_k + 1)
            
            inertia = []
            silhouette_scores = []
            
            from sklearn.metrics import silhouette_score
            
            print("\nDeterminazione del numero ottimale di cluster...")
            for k in k_range:
                kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
                kmeans.fit(scaled_features)
                inertia.append(kmeans.inertia_)
                
                # Calcola il silhouette score
                labels = kmeans.labels_
                if len(set(labels)) > 1:  # Controlla che ci sia più di un cluster
                    silhouette_scores.append(silhouette_score(scaled_features, labels))
                else:
                    silhouette_scores.append(0)
                    
                print(f"k={k}: inertia={kmeans.inertia_:.2f}, silhouette={silhouette_scores[-1]:.4f}")
            
            # Visualizzazione del metodo del gomito
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 2, 1)
            plt.plot(k_range, inertia, 'bo-')
            plt.title('Metodo del Gomito per K Ottimale')
            plt.xlabel('Numero di Cluster (k)')
            plt.ylabel('Inerzia')
            plt.grid(True)
            
            # Visualizzazione silhouette scores
            plt.subplot(1, 2, 2)
            plt.plot(k_range, silhouette_scores, 'ro-')
            plt.title('Silhouette Score per K')
            plt.xlabel('Numero di Cluster (k)')
            plt.ylabel('Silhouette Score')
            plt.grid(True)
            
            plt.tight_layout()
            plt.show()
            
            # Consiglia il k ottimale
            best_silhouette_idx = np.argmax(silhouette_scores)
            k_silhouette = k_range[best_silhouette_idx]
            
            # Stima il punto di gomito
            from kneed import KneeLocator
            try:
                kneedle = KneeLocator(k_range, inertia, curve='convex', direction='decreasing')
                k_elbow = kneedle.elbow
                print(f"\nK ottimale suggerito dal metodo del gomito: {k_elbow}")
                print(f"K ottimale suggerito dal silhouette score: {k_silhouette}")
            except:
                k_elbow = None
                print(f"\nK ottimale suggerito dal silhouette score: {k_silhouette}")
            
            # Suggerimento
            suggested_k = k_silhouette if k_silhouette else (k_elbow if k_elbow else 3)
            print(f"Suggerimento: utilizzare k={suggested_k}")
            
            # Chiedi all'utente il numero di cluster
            try:
                k = int(input(f"\nInserisci il numero di cluster da utilizzare (suggerito {suggested_k}): "))
                if k < 2 or k > max_k:
                    print(f"Numero di cluster non valido, uso k={suggested_k} come default")
                    k = suggested_k
            except:
                print(f"Input non valido, uso k={suggested_k} come default")
                k = suggested_k
            
            # Applicazione K-Means con k scelto
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            df_clustered = df.copy()
            df_clustered['CLUSTER'] = kmeans.fit_predict(scaled_features)
            
            # Analisi dei cluster
            print("\nAnalisi dei cluster:")
            # Include sia variabili usate nel clustering che altre di interesse
            analysis_cols = list(set(selected_features + ['ETA', 'DATI_CONSUMATI', 'TARIFFA_MENSILE', 'COSTO_PER_GB']))
            analysis_cols = [col for col in analysis_cols if col in df_clustered.columns]
            
            # Statistiche dettagliate per cluster
            cluster_stats = df_clustered.groupby('CLUSTER')[analysis_cols].agg([
                'mean', 'median', 'std', 'min', 'max', 'count'
            ])
            
            # Statistiche semplificate
            cluster_summary = df_clustered.groupby('CLUSTER')[analysis_cols].agg({
                col: ['mean', 'count'] for col in analysis_cols
            })
            
            print("\nRiepilogo dei cluster:")
            print(cluster_summary)
            
            # Visualizzazione 2D dei cluster
            if len(selected_features) >= 2:
                plt.figure(figsize=(10, 8))
                scatter = plt.scatter(
                    df_clustered[selected_features[0]], 
                    df_clustered[selected_features[1]],
                    c=df_clustered['CLUSTER'],
                    cmap='viridis',
                    s=50,
                    alpha=0.6
                )
                plt.title(f'Clustering K-Means con {k} Cluster')
                plt.xlabel(selected_features[0])
                plt.ylabel(selected_features[1])
                plt.colorbar(scatter, label='Cluster')
                plt.tight_layout()
                plt.show()
            
            # Visualizzazione 3D se ci sono almeno 3 feature
            if len(selected_features) >= 3:
                try:
                    from mpl_toolkits.mplot3d import Axes3D
                    
                    fig = plt.figure(figsize=(10, 8))
                    ax = fig.add_subplot(111, projection='3d')
                    
                    # Plot dei punti
                    scatter = ax.scatter(
                        df_clustered[selected_features[0]], 
                        df_clustered[selected_features[1]], 
                        df_clustered[selected_features[2]],
                        c=df_clustered['CLUSTER'],
                        cmap='viridis',
                        s=50,
                        alpha=0.6
                    )
                    
                    # Etichette
                    ax.set_xlabel(selected_features[0])
                    ax.set_ylabel(selected_features[1])
                    ax.set_zlabel(selected_features[2])
                    plt.title(f'Clustering K-Means 3D con {k} Cluster')
                    
                    # Legenda
                    plt.colorbar(scatter, ax=ax, label='Cluster')
                    
                    plt.tight_layout()
                    plt.show()
                except Exception as e:
                    print(f"Impossibile creare grafico 3D: {e}")
            
            # PCA per visualizzazione con più di 3 feature
            if len(selected_features) > 3:
                from sklearn.decomposition import PCA
                
                pca = PCA(n_components=2)
                principalComponents = pca.fit_transform(scaled_features)
                
                plt.figure(figsize=(10, 8))
                scatter = plt.scatter(
                    principalComponents[:, 0], 
                    principalComponents[:, 1],
                    c=df_clustered['CLUSTER'],
                    cmap='viridis',
                    s=50,
                    alpha=0.6
                )
                plt.title(f'Visualizzazione PCA dei {k} Cluster')
                plt.xlabel('Componente Principale 1')
                plt.ylabel('Componente Principale 2')
                plt.colorbar(scatter, label='Cluster')
                plt.tight_layout()
                plt.show()
                
                # Mostra quanta varianza è spiegata dai componenti
                explained_var = pca.explained_variance_ratio_
                print(f"\nVarianza spiegata dalle componenti PCA: {explained_var[0]:.2%} e {explained_var[1]:.2%}")
            
            # Distribuzione delle variabili categoriche per cluster
            if 'CONSUMO_CATEGORIA' in df_clustered.columns:
                plt.figure(figsize=(12, 6))
                pd.crosstab(df_clustered['CLUSTER'], df_clustered['CONSUMO_CATEGORIA'], 
                            normalize='index').plot(kind='bar', stacked=True)
                plt.title('Distribuzione delle Categorie di Consumo per Cluster')
                plt.ylabel('Proporzione')
                plt.xticks(rotation=0)
                plt.tight_layout()
                plt.show()
            
            # Interpretazione dei cluster
            print("\nInterpretazione dei cluster:")
            for i in range(k):
                print(f"\nCluster {i}:")
                # Mostra le medie di ogni variabile per il cluster
                cluster_means = df_clustered[df_clustered['CLUSTER'] == i][analysis_cols].mean()
                # Confronta con la media globale
                global_means = df_clustered[analysis_cols].mean()
                diff_percent = ((cluster_means - global_means) / global_means * 100).round(1)
                
                # Crea una tabella con medie e differenze percentuali
                comparison = pd.DataFrame({
                    'Cluster Mean': cluster_means.round(2),
                    'Global Mean': global_means.round(2),
                    'Diff %': diff_percent
                })
                print(comparison)
                
                # Identifica caratteristiche distintive (oltre ±20% dalla media)
                distinctive = diff_percent[abs(diff_percent) > 20].sort_values(ascending=False)
                if not distinctive.empty:
                    print("\nCaratteristiche distintive:")
                    for var, diff in distinctive.items():
                        direction = "superiore" if diff > 0 else "inferiore"
                        print(f"- {var}: {abs(diff):.1f}% {direction} alla media")
            
            return df_clustered
        except Exception as e:
            print(f"Errore nel clustering: {e}")
            import traceback
            traceback.print_exc()
            return None
    else:
        print("Nessun dato caricato")
        return None

# Funzione per esportare dati
def export_data(df):
    if df is not None:
        print("\nOpzioni di esportazione:")
        print("1. CSV")
        print("2. Excel")
        print("3. JSON")
        print("4. Pickle (per grandi dataset)")
        
        choice = input("Seleziona il formato (1-4): ")
        filename = input("Inserisci il nome del file (senza estensione): ")
        
        try:
            if choice == '1':
                file_path = f"{filename}.csv"
                df.to_csv(file_path, index=False)
                print(f"Dati esportati con successo in {file_path}")
            elif choice == '2':
                file_path = f"{filename}.xlsx"
                df.to_excel(file_path, index=False)
                print(f"Dati esportati con successo in {file_path}")
            elif choice == '3':
                file_path = f"{filename}.json"
                df.to_json(file_path, orient='records')
                print(f"Dati esportati con successo in {file_path}")
            elif choice == '4':
                file_path = f"{filename}.pkl"
                df.to_pickle(file_path)
                print(f"Dati esportati con successo in {file_path}")
            else:
                print("Formato non valido")
                
            # Visualizza le dimensioni del file
            if os.path.exists(file_path):
                size_bytes = os.path.getsize(file_path)
                if size_bytes < 1024:
                    size_str = f"{size_bytes} bytes"
                elif size_bytes < 1024 * 1024:
                    size_str = f"{size_bytes/1024:.1f} KB"
                else:
                    size_str = f"{size_bytes/(1024*1024):.1f} MB"
                    
                print(f"Dimensione del file: {size_str}")
        except Exception as e:
            print(f"Errore durante l'esportazione: {e}")
    else:
        print("Nessun dato disponibile per l'esportazione")

# Funzione per pulire lo schermo
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu principale
def main():
    # Prova a trovare il file prima
    base_dir = os.path.dirname(os.path.abspath(__file__))
    possible_paths = [
        r'clienti.csv',  # Nella directory corrente
        r'CorsoPython\Giorno 17 23 -04\ESERCITAZIONE telecomunicazioni\clienti.csv',  # Percorso relativo originale
        os.path.join(base_dir, 'clienti.csv')  # Nella stessa cartella dello script
    ]
    
    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            print(f"File trovato: {path}")
            break
    
    if not file_path:
        file_path = r'clienti.csv'  # Default se non trovato
        print(f"File non trovato automaticamente. Utilizzo path predefinito: {file_path}")
    
    # Variabile per memorizzare il dataframe
    df = None
    df_processed = None
    
    # Loop del menu
    while True:
        clear_screen()
        print("\nANALISI DATI TELECOMUNICAZIONI")
        print("1. Carica dati")
        print("2. Visualizza dati")
        print("3. Analisi descrittiva")
        print("4. Pulizia dati")
        print("5. Creazione nuove features")
        print("6. Analisi correlazioni")
        print("7. Test ANOVA (confronto consumo per età)")
        print("8. Test Chi-Quadrato (età vs consumo)")
        print("9. Regressione Logistica (previsione churn)")
        print("10. Clustering K-Means (segmentazione clienti)")
        print("11. Esporta dati")
        print("0. Esci")
        
        choice = input("\nScegli un'opzione (0-11): ")
        
        if choice == '0':
            print("\nChiusura del programma...")
            break
            
        elif choice == '1':
            # Chiedi il percorso se necessario
            custom_path = input(f"Inserisci il percorso del file CSV [Enter per {file_path}]: ")
            if custom_path.strip():
                file_path = custom_path
                
            df = load_data(file_path)
            if df is not None:
                df_processed = df.copy()  # Inizializza con i dati originali
            input("\nPremi Enter per continuare...")
            
        elif choice == '2':
            data_to_show = df_processed if df_processed is not None else df
            display_data(data_to_show)
            input("\nPremi Enter per continuare...")
            
        elif choice == '3':
            data_to_analyze = df_processed if df_processed is not None else df
            descriptive_analysis(data_to_analyze)
            input("\nPremi Enter per continuare...")
            
        elif choice == '4':
            if df is not None:
                df_processed = clean_data(df)
                print("\nDati puliti e memorizzati")
            else:
                print("\nNessun dato caricato. Carica i dati prima di procedere.")
            input("\nPremi Enter per continuare...")
            
        elif choice == '5':
            if df_processed is not None:
                df_processed = create_features(df_processed)
                print("\nFeatures create e memorizzate")
            else:
                print("\nNessun dato disponibile. Carica e pulisci i dati prima di procedere.")
            input("\nPremi Enter per continuare...")
            
        elif choice == '6':
            correlation_analysis(df_processed)
            input("\nPremi Enter per continuare...")
            
        elif choice == '7':
            anova_test(df_processed)
            input("\nPremi Enter per continuare...")
            
        elif choice == '8':
            chi_square_test(df_processed)
            input("\nPremi Enter per continuare...")
            
        elif choice == '9':
            logistic_regression(df_processed)
            input("\nPremi Enter per continuare...")
            
        elif choice == '10':
            df_clustered = clustering_kmeans(df_processed)
            if df_clustered is not None:
                choice = input("\nVuoi utilizzare i dati con i cluster per le analisi successive? (s/n): ")
                if choice.lower() in ['s', 'si', 'sì', 'y', 'yes']:
                    df_processed = df_clustered
                    print("Dataset aggiornato con i cluster")
            input("\nPremi Enter per continuare...")
            
        elif choice == '11':
            export_data(df_processed)
            input("\nPremi Enter per continuare...")
            
        else:
            print("\nOpzione non valida. Riprova.")
            input("\nPremi Enter per continuare...")

# Esecuzione del programma
if __name__ == "__main__":
    main()