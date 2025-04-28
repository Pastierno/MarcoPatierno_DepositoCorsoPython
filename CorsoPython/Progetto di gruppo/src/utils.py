def with_int_input(prompt: str, default: int = 10):
    """
    Decoratore per ottenere un input intero da passare come argomento alla funzione.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                value = int(input(f"{prompt} (default {default}): ") or default)
            except ValueError:
                print(f"Invalid input. Using default value: {default}")
                value = default
            return func(*args, value=value, **kwargs)
        return wrapper
    return decorator


def with_optional_input(prompt: str, arg_name: str = "input_value", allow_empty: bool = False):
    """
    Decoratore per ottenere un input opzionale e passarlo alla funzione.
    
    Se allow_empty è True, passa il valore vuoto ('') così com'è.
    Altrimenti, converte le stringhe vuote in None.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = input(f"{prompt} (premi Invio per saltare): ")
            if not allow_empty and value == "":
                value = None
            kwargs[arg_name] = value
            return func(*args, **kwargs)
        return wrapper
    return decorator


def with_header(title: str):
    """
    Decoratore per stampare un'intestazione prima dell'esecuzione della funzione.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("\n" + "-" * 50)
            print(title.upper())
            print("-" * 50)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def handle_invalid_choice(func):
    """
    Decoratore per intercettare e gestire opzioni non valide nei menu.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, KeyError):
            print("Invalid choice. Please try again.")
    return wrapper


def pause_after(func):
    """
    Decoratore per mettere in pausa dopo l'esecuzione della funzione.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        input("\nPress Enter to continue...")
        return result
    return wrapper
