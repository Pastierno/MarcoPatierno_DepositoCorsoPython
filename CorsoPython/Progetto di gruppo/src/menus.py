# Importazione dei decoratori personalizzati dal modulo utils
from src.utils import with_header, with_int_input, with_optional_input, handle_invalid_choice, pause_after
# L'utilizzo di handle_invalid_choice() come decoratore è opzionale 
# ---------------------- MENU: Analisi Generale ----------------------

# Decoratore che mostra un'intestazione ogni volta che si accede al menu
@with_header("GENERAL ANALYSIS MENU")
def general_analysis_menu(analizer):
    # Ciclo infinito per mostrare il menu finché l'utente non sceglie di uscire
    while True:
        print("1. Show top tracks")
        print("2. Show top artists")
        print("3. Show most streamed track")
        print("4. Show tracks by artist")
        print("5. Show tracks above stream threshold")
        print("6. Show artist track counts")
        print("7. Back to main menu")

        # Lettura della scelta dell'utente
        choice = input("\nSelect an option (1-7): ")
        match choice:
            case "1":
                show_top_tracks(analizer)
            case "2":
                show_top_artists(analizer)
            case "3":
                show_most_streamed(analizer)
            case "4":
                show_tracks_by_artist(analizer)
            case "5":
                show_tracks_above_threshold(analizer)
            case "6":
                show_artist_track_counts(analizer)
            case "7":
                break  # Uscita dal menu
            case _:
                print("Invalid choice. Please try again.")

# Funzione per mostrare le top tracce con input numerico e pausa finale
@with_int_input("How many tracks to show?", default=10)
@pause_after
def show_top_tracks(analizer, value):
    print(analizer.top_tracks(value))

@with_int_input("How many artists to show?", default=10)
@pause_after
def show_top_artists(analizer, value):
    print(analizer.top_artists(value))

@pause_after
def show_most_streamed(analizer):
    print(analizer.most_streamed_track())

@with_optional_input("Enter artist name", arg_name="artist")
@pause_after
def show_tracks_by_artist(analizer, artist):
    print(analizer.streams_by_artist(artist))

@with_int_input("Enter stream threshold", default=1000000)
@pause_after
def show_tracks_above_threshold(analizer, value):
    print(analizer.tracks_above_threshold(value))

@pause_after
def show_artist_track_counts(analizer):
    print(analizer.artists_track_count())

# ---------------------- MENU: Analisi Temporale ----------------------

@with_header("TEMPORAL ANALYSIS MENU")
def temporal_analysis_menu(analizer):
    while True:
        print("1. Filter by day")
        print("2. Daily streams since date")
        print("3. Top artists since date")
        print("4. Filter by month range")
        print("5. Top track in month/range")
        print("6. Top artists in month/range")
        print("7. Monthly streams")
        print("8. Back to main menu")

        choice = input("\nSelect an option (1-8): ")
        match choice:
            case "1":
                filter_by_day(analizer)
            case "2":
                daily_streams_since(analizer)
            case "3":
                top_artists_since(analizer)
            case "4":
                filter_by_month_range(analizer)
            case "5":
                top_track_in_month(analizer)
            case "6":
                top_artists_in_month(analizer)
            case "7":
                monthly_streams(analizer)
            case "8":
                break
            case _:
                print("Invalid choice. Please try again.")

@with_optional_input("Enter date (YYYY-MM-DD)", arg_name="day")
@pause_after
def filter_by_day(analizer, day):
    print(analizer.filter_by_day(day))

@with_optional_input("Enter start date (YYYY-MM-DD)", arg_name="day")
@pause_after
def daily_streams_since(analizer, day):
    print(analizer.daily_streams_custom(day))

@with_optional_input("Enter start date (YYYY-MM-DD)", arg_name="day")
@with_int_input("How many artists to show?", default=10)
@pause_after
def top_artists_since(analizer, value, day):
    print(analizer.top_artists_since(day, value))

@with_optional_input("Enter start month (YYYY-MM)", arg_name="start")
@with_optional_input("Enter end month (YYYY-MM, optional)", arg_name="end", allow_empty=True)
@pause_after
def filter_by_month_range(analizer, start, end):
    print(analizer.filter_by_month_range(start, end))

@with_optional_input("Enter start month (YYYY-MM)", arg_name="start")
@with_optional_input("Enter end month (YYYY-MM, optional)", arg_name="end", allow_empty=True)
@pause_after
def top_track_in_month(analizer, start, end):
    print(analizer.top_track_in_month(start, end))

@with_optional_input("Enter start month (YYYY-MM)", arg_name="start")
@with_optional_input("Enter end month (YYYY-MM, optional)", arg_name="end", allow_empty=True)
@with_int_input("How many artists to show?", default=10)
@pause_after
def top_artists_in_month(analizer, value, start, end):
    print(analizer.top_artists_in_month(start, end, value))

@with_optional_input("Enter start month (YYYY-MM)", arg_name="start")
@with_optional_input("Enter end month (YYYY-MM, optional)", arg_name="end", allow_empty=True)
@pause_after
def monthly_streams(analizer, start, end):
    print(analizer.monthly_streams(start, end))

# ---------------------- MENU: Statistiche ----------------------

@with_header("STATISTICAL ANALYSIS MENU")
def statistical_analysis_menu(stat_analyzer):
    while True:
        print("1. Mean")
        print("2. Median")
        print("3. Standard deviation")
        print("4. Variance")
        print("5. Minimum value")
        print("6. Maximum value")
        print("7. Correlation")
        print("8. Covariance")
        print("9. Skewness")
        print("10. Kurtosis")
        print("11. Quartiles")
        print("12. Interquartile range (IQR)")
        print("13. Distribution summary")
        print("14. Back to main menu")

        choice = input("\nSelect an option (1-14): ")
        match choice:
            case "1": mean(stat_analyzer)
            case "2": median(stat_analyzer)
            case "3": std_dev(stat_analyzer)
            case "4": variance(stat_analyzer)
            case "5": min_value(stat_analyzer)
            case "6": max_value(stat_analyzer)
            case "7": correlation(stat_analyzer)
            case "8": covariance(stat_analyzer)
            case "9": skewness(stat_analyzer)
            case "10": kurtosis(stat_analyzer)
            case "11": quartiles(stat_analyzer)
            case "12": iqr(stat_analyzer)
            case "13": distribution_summary(stat_analyzer)
            case "14": break
            case _: print("Invalid choice. Please try again.")

# Ogni funzione qui sotto è decorata con @pause_after per mostrare il risultato e poi mettere in pausa

@pause_after
def mean(stat_analyzer): print(stat_analyzer.mean())

@pause_after
def median(stat_analyzer): print(stat_analyzer.median())

@pause_after
def std_dev(stat_analyzer): print(stat_analyzer.std_dev())

@pause_after
def variance(stat_analyzer): print(stat_analyzer.variance())

@pause_after
def min_value(stat_analyzer): print(stat_analyzer.min_value())

@pause_after
def max_value(stat_analyzer): print(stat_analyzer.max_value())

@pause_after
def correlation(stat_analyzer): print(stat_analyzer.correlation())

@pause_after
def covariance(stat_analyzer): print(stat_analyzer.covariance())

@pause_after
def skewness(stat_analyzer): print(stat_analyzer.skewness())

@pause_after
def kurtosis(stat_analyzer): print(stat_analyzer.kurtosis())

@pause_after
def quartiles(stat_analyzer): print(stat_analyzer.quartiles())

@pause_after
def iqr(stat_analyzer): print(stat_analyzer.iqr())

@pause_after
def distribution_summary(stat_analyzer): print(stat_analyzer.distribution_summary())

# ---------------------- MENU: Visualizzazioni ----------------------

@with_header("VISUALIZATIONS MENU")
def visualizations_menu(visualizer):
    while True:
        print("1. Visualize top tracks")
        print("2. Visualize top artists")
        print("3. Visualize most streamed track")
        print("4. Visualize artist streams")
        print("5. Visualize tracks above threshold")
        print("6. Visualize artist track counts")
        print("7. Visualize daily streams")
        print("8. Visualize top artists since date")
        print("9. Visualize monthly streams")
        print("10. Visualize top tracks by month")
        print("11. Visualize top artists by month")
        print("12. Visualize position vs streams")
        print("13. Visualize streams pie chart")
        print("14. Show all visualizations")
        print("15. Back to main menu")

        choice = input("\nSelect an option (1-15): ")
        match choice:
            case "1": visualize_top_tracks(visualizer)
            case "2": visualize_top_artists(visualizer)
            case "3": visualizer.visualize_most_streamed_track()
            case "4": visualize_streams_by_artist(visualizer)
            case "5": visualize_tracks_above_threshold(visualizer)
            case "6": visualize_artist_track_count(visualizer)
            case "7": visualize_daily_streams(visualizer)
            case "8": visualize_top_artists_since(visualizer)
            case "9": visualize_monthly_streams(visualizer)
            case "10": visualize_top_tracks_month(visualizer)
            case "11": visualize_top_artists_month(visualizer)
            case "12": visualizer.visualize_position_vs_streams()
            case "13": visualize_streams_pie_chart(visualizer)
            case "14": visualizer.visualize_all()
            case "15": break
            case _: print("Invalid choice. Please try again.")

@with_int_input("How many tracks to visualize?", default=10)
def visualize_top_tracks(visualizer, value):
    visualizer.visualize_top_tracks(value)

@with_int_input("How many artists to visualize?", default=10)
def visualize_top_artists(visualizer, value):
    visualizer.visualize_top_artists(value)

@with_optional_input("Enter artist name", arg_name="artist")
def visualize_streams_by_artist(visualizer, artist):
    visualizer.visualize_streams_by_artist(artist)

@with_int_input("Enter stream threshold", default=1000000)
def visualize_tracks_above_threshold(visualizer, value):
    visualizer.visualize_tracks_above_threshold(value)

@with_int_input("Show top how many artists?", default=15)
def visualize_artist_track_count(visualizer, value):
    visualizer.visualize_artists_track_count(value)

@with_optional_input("Enter start date (YYYY-MM-DD)", arg_name="day")
@with_int_input("How many days to show?", default=30)
def visualize_daily_streams(visualizer, value, day):
    visualizer.visualize_daily_streams(day, value)

@with_optional_input("Enter start date (YYYY-MM-DD)", arg_name="day")
@with_int_input("How many artists to show?", default=10)
def visualize_top_artists_since(visualizer, value, day):
    visualizer.visualize_top_artists_since(day, value)

@with_optional_input("Enter start month (YYYY-MM)", arg_name="start")
@with_optional_input("Enter end month (YYYY-MM, optional)", arg_name="end", allow_empty=True)
def visualize_monthly_streams(visualizer, start, end):
    visualizer.visualize_monthly_streams(start, end)

@with_optional_input("Enter start month (YYYY-MM)", arg_name="start")
@with_optional_input("Enter end month (YYYY-MM, optional)", arg_name="end", allow_empty=True)
def visualize_top_tracks_month(visualizer, start, end):
    visualizer.visualize_top_track_in_month(start, end)

@with_optional_input("Enter start month (YYYY-MM)", arg_name="start")
@with_optional_input("Enter end month (YYYY-MM, optional)", arg_name="end", allow_empty=True)
@with_int_input("How many artists to show?", default=10)
def visualize_top_artists_month(visualizer, value, start, end):
    visualizer.visualize_top_artists_in_month(start, end, value)

@with_int_input("Show top how many artists?", default=7)
def visualize_streams_pie_chart(visualizer, value):
    visualizer.visualize_streams_pie_chart(value)

