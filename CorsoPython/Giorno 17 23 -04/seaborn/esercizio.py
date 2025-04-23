import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Creazione Dataframe
def create_dataframe(num_rows=1000):
    # Genero sesso (0 per femmine, 1 per maschi)
    gender = np.random.choice([0, 1], size=num_rows, p=[0.5, 0.5])
    
    # Genero età
    eta = np.random.normal(40, 12, size=num_rows)
    eta = np.clip(eta, 18, 75).astype(int)
    
    # Altezza dipende dal sesso (distribuzione normale)
    altezza = np.where(
        gender == 1,
        np.random.normal(175, 7, size=num_rows),  # maschi
        np.random.normal(163, 6, size=num_rows)   # femmine
    )
    altezza = np.clip(altezza, 145, 205).astype(int)
    
    # Peso correlato all'altezza e al sesso (BMI realistico + variabilità)
    bmi_base = np.random.normal(24, 4, size=num_rows)
    peso = bmi_base * (altezza/100)**2
    # Aggiungi variazione per età (persone più anziane tendono ad avere BMI più alto)
    peso += (eta - 30) * 0.1
    peso = np.clip(peso, 40, 130).astype(int)
    
    # Crea DataFrame
    data = {
        'altezza': altezza,
        'peso': peso,
        'eta': eta,
        'sesso': ['M' if g == 1 else 'F' for g in gender]
    }
    df = pd.DataFrame(data)
    
    # Aggiungi BMI come colonna calcolata
    df['bmi'] = df['peso'] / ((df['altezza']/100)**2)
    
    return df

# Normalizzazione dei dati numerici
def min_max(df):
    scaler = MinMaxScaler()
    numeric_cols = ['altezza', 'peso', 'eta', 'bmi']
    df_scaled = df.copy()
    df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df_scaled

# Funzione per aggiungere una colonna basata sul range specificato dall'utente
def add_range_column(df):
    print("\nAggiungi range personalizzato")
    
    # Scegli la variabile per il range
    print("Seleziona la variabile su cui applicare il range:")
    print("1. Età")
    print("2. Altezza")
    print("3. Peso")
    print("4. BMI")
    
    var_choice = input("Scelta (1-4): ")
    var_map = {'1': 'eta', '2': 'altezza', '3': 'peso', '4': 'bmi'}
    
    if var_choice not in var_map:
        print("Scelta non valida. Uso 'eta' come default.")
        var_choice = '1'
    
    selected_var = var_map[var_choice]
    
    # Mostra range disponibile
    min_val = df[selected_var].min()
    max_val = df[selected_var].max()
    print(f"Range disponibile per {selected_var}: {min_val} - {max_val}")
    
    # Ottieni il range dall'utente
    try:
        range_min = float(input(f"Inserisci il valore minimo per {selected_var}: "))
        range_max = float(input(f"Inserisci il valore massimo per {selected_var}: "))
        
        # Validazione input
        if range_min >= range_max:
            print("Il minimo deve essere inferiore al massimo. Uso valori predefiniti.")
            range_min = min_val + (max_val - min_val) * 0.3  # 30% del range
            range_max = min_val + (max_val - min_val) * 0.7  # 70% del range
    except:
        print("Input non valido. Uso valori predefiniti.")
        range_min = min_val + (max_val - min_val) * 0.3  # 30% del range
        range_max = min_val + (max_val - min_val) * 0.7  # 70% del range
    
    # Crea una nuova colonna che indica se il valore è nel range specificato
    range_col_name = f"{selected_var}_in_range"
    df[range_col_name] = (df[selected_var] >= range_min) & (df[selected_var] <= range_max)
    
    # Crea una colonna categorica per il range
    range_cat_name = f"{selected_var}_categoria"
    conditions = [
        (df[selected_var] < range_min),
        (df[selected_var] >= range_min) & (df[selected_var] <= range_max),
        (df[selected_var] > range_max)
    ]
    choices = ['Sotto range', 'Nel range', 'Sopra range']
    df[range_cat_name] = np.select(conditions, choices, default='Sconosciuto')
    
    print(f"Colonne aggiunte: '{range_col_name}' e '{range_cat_name}'")
    print(f"Statistiche per i record nel range ({range_min}-{range_max}):")
    print(df[df[range_col_name]].describe())
    
    return df, selected_var, range_min, range_max, range_col_name, range_cat_name

def main():
    df = create_dataframe()
    df_scaled = min_max(df)
    
    # Variabili per il range
    range_applied = False
    selected_var = None
    range_min = None
    range_max = None
    range_col_name = None
    range_cat_name = None
    
    while True:
        print("\n1. Scatter plot altezza vs peso (originale)")
        print("2. Scatter plot altezza vs peso (normalizzato)")
        print("3. Distribuzione di altezza, peso ed età")
        print("4. Box plot per variabili numeriche")
        print("5. Scatter plot per sesso con età come dimensione")
        print("6. Matrice di correlazione")
        print("7. Pair plot di tutte le variabili")
        print("8. Distribuzione BMI per sesso")
        print("9. Relazione età-peso con regression line")
        print("10. Aggiungi filtro per range personalizzato")
        if range_applied:
            print("11. Visualizza dati con filtro per range")
        print("0. Esci")
        
        choice = input("\nScegli un'opzione: ")
        
        if choice == '1':
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x='altezza', y='peso', hue='sesso', alpha=0.7)
            plt.title('Relazione tra Altezza e Peso')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
    
        elif choice == '2':
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df_scaled, x='altezza', y='peso', hue='sesso', alpha=0.7)
            plt.title('Relazione tra Altezza e Peso (Normalizzata)')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            
        elif choice == '3':
            # Distribuzione delle variabili con KDE plots
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            
            sns.histplot(data=df, x='altezza', kde=True, ax=axes[0], hue='sesso')
            axes[0].set_title('Distribuzione Altezza')
            
            sns.histplot(data=df, x='peso', kde=True, ax=axes[1], hue='sesso')
            axes[1].set_title('Distribuzione Peso')
            
            sns.histplot(data=df, x='eta', kde=True, ax=axes[2], hue='sesso')
            axes[2].set_title('Distribuzione Età')
            
            plt.tight_layout()
            plt.show()
            
        elif choice == '4':
            # Box plots per le variabili numeriche divisi per sesso
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            
            sns.boxplot(data=df, x='sesso', y='altezza', ax=axes[0])
            axes[0].set_title('Distribuzione Altezza per Sesso')
            
            sns.boxplot(data=df, x='sesso', y='peso', ax=axes[1])
            axes[1].set_title('Distribuzione Peso per Sesso')
            
            sns.boxplot(data=df, x='sesso', y='bmi', ax=axes[2])
            axes[2].set_title('Distribuzione BMI per Sesso')
            
            plt.tight_layout()
            plt.show()
            
        elif choice == '5':
            # Scatter plot con dimensione punti basata sull'età
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                data=df, 
                x='altezza', 
                y='peso', 
                hue='sesso', 
                size='eta',  # Dimensione basata sull'età
                sizes=(20, 200),  # Range delle dimensioni
                alpha=0.7
            )
            plt.title('Relazione tra Altezza, Peso, Età e Sesso')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            
        elif choice == '6':
            # Matrice di correlazione
            plt.figure(figsize=(8, 6))
            corr = df.select_dtypes(include=[np.number]).corr()
            mask = np.triu(np.ones_like(corr, dtype=bool))
            sns.heatmap(corr, annot=True, mask=mask, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
            plt.title('Matrice di Correlazione')
            plt.show()
            
        elif choice == '7':
            # Pair plot per visualizzare tutte le relazioni tra variabili
            sns.pairplot(df, hue='sesso', height=2.5)
            plt.suptitle('Pair Plot di Tutte le Variabili', y=1.02)
            plt.show()
            
        elif choice == '8':
            # Distribuzione del BMI per sesso
            plt.figure(figsize=(10, 6))
            sns.kdeplot(data=df, x='bmi', hue='sesso', fill=True, common_norm=False)
            plt.title('Distribuzione del BMI per Sesso')
            plt.axvline(x=18.5, color='red', linestyle='--', label='Sottopeso (<18.5)')
            plt.axvline(x=25, color='orange', linestyle='--', label='Sovrappeso (>25)')
            plt.axvline(x=30, color='red', linestyle='--', label='Obesità (>30)')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            
        elif choice == '9':
            # Relazione età-peso con linea di regressione
            plt.figure(figsize=(10, 6))
            sns.regplot(data=df, x='eta', y='peso', scatter_kws={'alpha':0.5})
            plt.title('Relazione tra Età e Peso con Linea di Regressione')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
        
        elif choice == '10':
            # Aggiungi colonna basata sul range specificato dall'utente
            df, selected_var, range_min, range_max, range_col_name, range_cat_name = add_range_column(df)
            range_applied = True
            # Aggiorna anche il dataframe scalato
            df_scaled = min_max(df)
            
        elif choice == '11' and range_applied:
            # Visualizza dati con range applicato
            
            # Grafico 1: Scatter plot colorato per range
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                data=df, 
                x='altezza', 
                y='peso', 
                hue=range_cat_name,
                style='sesso',
                alpha=0.7
            )
            plt.title(f'Relazione tra Altezza e Peso con Categoria di {selected_var}')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            
            # Grafico 2: Distribuzione della variabile con evidenziato il range
            plt.figure(figsize=(12, 6))
            ax = sns.histplot(data=df, x=selected_var, kde=True)
            plt.axvline(x=range_min, color='red', linestyle='--', label=f'Min: {range_min}')
            plt.axvline(x=range_max, color='red', linestyle='--', label=f'Max: {range_max}')
            plt.fill_between([range_min, range_max], 0, 
                           ax.get_ylim()[1], color='green', alpha=0.2, label='Range selezionato')
            plt.title(f'Distribuzione di {selected_var} con Range Evidenziato')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            
            # Grafico 3: Box plot che confronta i dati nel range e fuori dal range
            plt.figure(figsize=(12, 6))
            sns.boxplot(data=df, x=range_cat_name, y='bmi')
            plt.title(f'Distribuzione del BMI per Categoria di {selected_var}')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            
            # Grafico 4: Conteggio per categoria
            plt.figure(figsize=(8, 6))
            count_data = df[range_cat_name].value_counts().reset_index()
            count_data.columns = [range_cat_name, 'Conteggio']
            sns.barplot(data=count_data, x=range_cat_name, y='Conteggio')
            plt.title(f'Conteggio per Categoria di {selected_var}')
            for i, count in enumerate(count_data['Conteggio']):
                plt.text(i, count + 5, str(count), ha='center')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            
        elif choice == '0':
            print("Grazie per aver utilizzato il visualizzatore dati. Arrivederci!")
            break
            
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()