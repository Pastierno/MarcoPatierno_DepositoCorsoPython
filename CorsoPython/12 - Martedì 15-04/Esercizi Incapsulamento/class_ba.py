import sqlite3

class BankAccount():
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
        
    def deposit(self, amount): # Metodo per depositare denaro
        # Controlla se l'importo è positivo
        if amount > 0:
            self.__balance += amount
            print(f"Depositato: {amount}")
            
        else:
            print("Il valore deve essere positivo")
            
    
    def withdraw(self, amount):# Metodo per prelevare denaro
        # Controlla se l'importo è positivo e non supera il saldo
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Prelevato: {amount}")
        else:
            print("Il valore deve essere positivo e non può superare il saldo")
            
    def get_balance(self):
        return self.__balance # Metodo per ottenere il saldo attuale
    
    def get_owner(self):
        return self.__owner # Metodo per ottenere il nome del proprietario
# Esempio di utilizzo della classe BankAccount

# conto = BankAccount("Michele Spaghetto", 1000)

# conto.deposit(20)
# conto.withdraw(50)
# #conto.withdraw(2000)  # Questo darà errore perché il prelievo supera il saldo
# print(conto.get_balance())