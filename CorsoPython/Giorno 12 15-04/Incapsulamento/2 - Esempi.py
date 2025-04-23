# Variabile globale
num = 10

def external_function():
    # Variabile locale
    num = 5
    print("num (locale):", num)  # Stampa 5
    
    def internal_function():
        # Variabile non locale
        nonlocal num
        num = 3
        print("num (non locale):", num)
    
    internal_function()

print("num (globale):", num)  # Stampa 10
external_function()
print("num (globale):", num)  # Stampa 10
# La variabile num è stata modificata all'interno della funzione interna, ma non ha influenzato la variabile globale