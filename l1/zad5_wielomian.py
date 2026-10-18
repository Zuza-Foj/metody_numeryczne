import cProfile

def wielomian(x):
    w = 6*x**4 + 5*x**3 - 13*x**2 + x + 1
    return w

def wyliczanie_wart():
    dx = 0.0001
    wyn = []
    for i in range(200001):
        x = -10 + i * dx
        y = wielomian(x)
        wyn.append((x, y))
    print('l. obliczonych wartosci:', len(wyn))
    print('pierwszy wyn:', wyn[0])
    print('ostatni wyn:', wyn[-1])

if __name__=="__main__":
    cProfile.run("wyliczanie_wart()", sort='cumtime')

'''Krótkie wnioski: Wersja Hornera powinna być szybsza. 
Wprost ze wzoru potrzeba 4 potęg i 4 dodawań, a w schemacie Hornera są tylko 
4 mnożenia i 4 dodawania. W Pythonie operator ** jest wolniejszy od zwykłego 
mnożenia.'''