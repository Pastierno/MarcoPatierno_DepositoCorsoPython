import joblib
import pandas as pd

# Percorsi ai file serializzati del modello e della lista di malattie\MODEL_PATH = "disease_pipeline.pkl"
DISEASE_LIST_PATH = r"C:\Users\fabri\Desktop\MarcoPatierno_DepositoCorsoPython\env\Giorno 21 05-05\esercitazione\notebook\disease_list.pkl"
MODEL_PATH = r"C:\Users\fabri\Desktop\MarcoPatierno_DepositoCorsoPython\env\Giorno 21 05-05\esercitazione\notebook\disease_pipeline.pkl"

def menu():
    # Carica il modello e la lista delle malattie
    try:
        model = joblib.load(MODEL_PATH)
        disease_list = joblib.load(DISEASE_LIST_PATH)
    except FileNotFoundError:
        print("✖ Modello non trovato. Assicurati di aver eseguito il notebook e generato i file .pkl.")
        return

    while True:
        print("\n=== MENU ===")
        print("1) Predici la malattia più probabile")
        print("0) Esci")
        choice = input("Seleziona un'opzione: ")

        if choice == "1":
            country = input("Inserisci il paese: ")
            year_input = input("Inserisci l'anno (es. 2025): ")
            if not year_input.isdigit():
                print("✖ Anno non valido, deve essere un numero intero.")
                continue
            year = int(year_input)

            # Costruisci DataFrame per tutte le malattie
            X_new = pd.DataFrame([
                {"Country/Territory": country, "Year": year, "Disease": d}
                for d in disease_list
            ])
            # Predici le probabilità
            probs = model.predict(X_new)
            idx_max = probs.argmax()

            top_disease = disease_list[idx_max]
            top_prob    = probs[idx_max]

            print(f"\n→ Malattia più probabile in {country} nel {year}: {top_disease} ({top_prob:.2%})\n")

        elif choice == "0":
            print("Arrivederci!")
            break

        else:
            print("✖ Opzione non valida, riprova.")

if __name__ == "__main__":
    menu()
