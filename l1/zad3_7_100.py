'''7/100 * 100 - 7 = 0'''

print(7/100 * 100 - 7)

wyn = []
for i in range(50):
    wyn.append(i/100 * 100 - i)

problemy = []
for i in range(len(wyn)):
    if wyn[i] != 0:
        problemy.append(i)

print(problemy)

'''Problemy są z wielokrotnościami 7 oraz liczbą 29.
Dlaczego?
Błąd zaokrąglenia ułamka 7/100 (który jest okresowy) powpduje, że wychodzi coś bliskiego zeru,
ale nie zero. Błąd ten wynika z tego, że pamięć komputera jest ograniczona i nie może 
przechować 7/100 jako dokładną wartość, bo rozwinięcie jest nieskończone.

W reszcie przypadków np. 3/100 * 100 - 3, błędy wynikające z dzielenia i z mnożenia się skompensowały.'''