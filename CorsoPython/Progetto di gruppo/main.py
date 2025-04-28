from src.data_analysis import DataframeAnalizer
from src.data_cleaning import dataframe
from src.statistical_analysis import StatisticalAnalyzer
from src.data_visualization import Visualizer
from src.menus import general_analysis_menu, temporal_analysis_menu, statistical_analysis_menu, visualizations_menu


def main():
    # Caricamento dei dati e inizializzazione delle classi
    df = dataframe()
    analizer = DataframeAnalizer(df)
    stat_analyzer = StatisticalAnalyzer(df.select_dtypes(include='number'))
    visualizer = Visualizer(analizer)

    # Dizionario delle opzioni del menu principale
    menu_options = {
        "1": ("Analisi Generale", lambda: general_analysis_menu(analizer)),
        "2": ("Analisi Temporale", lambda: temporal_analysis_menu(analizer)),
        "3": ("Analisi Statistica", lambda: statistical_analysis_menu(stat_analyzer)),
        "4": ("Visualizzazioni", lambda: visualizations_menu(visualizer)),
        "5": ("Esci", None)
    }

    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPALE - ANALISI DATI SPOTIFY")
        print("="*50)
        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")
        
        choice = input("\nSeleziona un'opzione (1-5): ")

        if choice in menu_options:
            if choice == "5":
                print("Uscita dal programma...")
                break
            else:
                # Esecuzione della funzione corrispondente alla scelta dell'utente
                menu_options[choice][1]()
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
