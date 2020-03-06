def even_numbers(werte):
    start_wert = min(werte)
    counter = 0
    ergebnisliste = []
    for v in werte:
        if (v % 2 == 0):
            counter += 1
            ergebnisliste.append(v)
    return counter, ergebnisliste

werte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = even_numbers(werte)

print(y)
