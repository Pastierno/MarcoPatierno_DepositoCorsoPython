class Computer():
    def __init__(self):
        self.__processore = "Intel i5" # Attributo privato
        
    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore = processore
        
pc = Computer()
print(pc.get_processore())
pc.set_processore("Intel i7")
print(pc.get_processore())
# pc.__processore = "AMD" # Questo darà errore perché __processore è privato