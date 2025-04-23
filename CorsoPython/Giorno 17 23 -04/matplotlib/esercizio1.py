import pandas as pd
import matplotlib.pyplot as plt
import random

# Genero dati di temperatura giornaliera per un mese in modo casuale ma realistico
# Temperature tra 15 e 30 gradi con piccole variazioni giornaliere
temps = []
current_temp = random.uniform(20, 25)  # Temperatura iniziale casuale

for i in range(30):
    # Aggiungo una variazione casuale limitata rispetto al giorno precedente (-2 a +2 gradi)
    current_temp += random.uniform(-2, 2)
    
    # Mantengo la temperatura in un range
    current_temp = max(15, min(30, current_temp))
    temps.append(round(current_temp, 1))

data = {
    'Giorno': [i for i in range(1, 31)],
    'Temperatura': temps
}
df = pd.DataFrame(data)

def menu():
    while True:
        print("\n1. Visualizza il grafico delle temperature")
        print("2. Temperatura massima e minima")
        print("3. Temperatura media")
        print("4. Mediana delle temperature")
        print("5. Esci")
        choice = input("Scegli un'opzione: ")
        
        if choice == '1':
            plt.figure(figsize=(10, 5))
            plt.plot(df['Giorno'], df['Temperatura'], marker='o', color='green')
            plt.title('Temperatura Giornaliera')
            plt.xlabel('Giorno')
            plt.ylabel('Temperatura (°C)')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.show()
            
        elif choice == '2':
            max_temp = df['Temperatura'].max()
            min_temp = df['Temperatura'].min()
            max_day = df.loc[df['Temperatura'] == max_temp, 'Giorno'].values[0]
            min_day = df.loc[df['Temperatura'] == min_temp, 'Giorno'].values[0]
            
            print(f"Temperatura massima: {max_temp}°C (Giorno {max_day})")
            print(f"Temperatura minima: {min_temp}°C (Giorno {min_day})")
            
            # Grafico con evidenziati massimo e minimo
            plt.figure(figsize=(10, 5))
            plt.plot(df['Giorno'], df['Temperatura'], marker='o', color='green')
            
            # Evidenzio il massimo con un punto rosso più grande
            plt.scatter(max_day, max_temp, color='red', s=100, label=f'Max: {max_temp}°C')
            
            # Evidenzio il minimo con un punto blu più grande
            plt.scatter(min_day, min_temp, color='blue', s=100, label=f'Min: {min_temp}°C')
            
            plt.title('Temperature Giornaliere con Massimo e Minimo')
            plt.xlabel('Giorno')
            plt.ylabel('Temperatura (°C)')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.show()
            
            # Grafico a barre per max e min
            plt.figure(figsize=(8, 5))
            plt.bar(['Minima', 'Massima'], [min_temp, max_temp], color=['blue', 'red'], width=0.5)
            plt.title('Temperature Minima e Massima')
            plt.ylabel('Temperatura (°C)')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            # Aggiungo etichette con i valori
            for i, v in enumerate([min_temp, max_temp]):
                plt.text(i, v + 0.1, f"{v}°C", ha='center')
                
            plt.show()
            
        elif choice == '3':
            mean_temp = df['Temperatura'].mean()
            print(f"Temperatura media: {mean_temp:.2f}°C")
            
            # Grafico semplice con linea della media
            plt.figure(figsize=(10, 5))
            plt.plot(df['Giorno'], df['Temperatura'], marker='o', color='green')
            
            # Aggiungo linea orizzontale per la media
            plt.axhline(y=mean_temp, color='red', linestyle='--', label=f'Media: {mean_temp:.2f}°C')
            
            plt.title('Temperature Giornaliere con Media')
            plt.xlabel('Giorno')
            plt.ylabel('Temperatura (°C)')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.show()
            
        elif choice == '4':
            median_temp = df['Temperatura'].median()
            print(f"Mediana delle temperature: {median_temp:.2f}°C")
            
            # Grafico semplice con linea della mediana
            plt.figure(figsize=(10, 5))
            plt.plot(df['Giorno'], df['Temperatura'], marker='o', color='#3498db')
            
            # Aggiungo linea orizzontale per la mediana
            plt.axhline(y=median_temp, color='green', linestyle='--', label=f'Mediana: {median_temp:.2f}°C')
            
            plt.title('Temperature Giornaliere con Mediana')
            plt.xlabel('Giorno')
            plt.ylabel('Temperatura (°C)')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend()
            plt.show()
            
        elif choice == '5':
            print("Ciao!")
            break
        
        else:
            print("Opzione non valida. Riprova.")
        
if __name__ == "__main__":
    menu()