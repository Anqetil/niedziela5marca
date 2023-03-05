# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = {1234, 3476, 3098, 4544, 3423}
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

#sprawdzamy ile osob chorowalo w ostatnim roku na krzykach
print('chorzy w ostatnim roku z krzyków to =', krzyki.intersection(chorzy_rok))
print('liczba =', len(krzyki.intersection(chorzy_rok)))

#sprawdzamy ile mieszka w sumie centrum i krzykach
#union = suma
print('liczba ludzi w centrum i na krykach to', len(centrum.union(krzyki)))
centrum.union(krzyki)

#difference - róznica 2 zbiorów a.difference(b)
#kazdy,kto chorowal w ostatnim mieisacu, jednoczesnie chorowal w ostatnim roku

if len(chorzy_miesiac.difference(chorzy_rok)) == 0:
    print('ok')
else:
    print('problem', chorzy_miesiac.difference(chorzy_rok))

#nikt nie powienien mieszkac jednoczesnie w centrum i na krzykach
#- jesli tak trzeba usunąć
# zbior.remove(element)

if len(krzyki.intersection(centrum)) != 0:
    x = input('usunac z centrum (C), czy z krzykow (K)')
    duplikaty = krzyki.intersection(centrum)
    if x.lower() == 'k':
        krzyki = krzyki.difference(duplikaty)
    elif x.lower() == 'c':
        for pesel in duplikaty:
            centrum.remove(pesel)

    else:
        print('zly wybor')
        print('sprzawdzamduplikaty:', krzyki.intersection((centrum)))

#kazdy: chory, zdrowy, z krzykow i z centrum, powinien być w bazie nfz
#jesli nie ma trzeba dopisać

pozaNFZ = chorzy_rok.union(chorzy_miesiac.union(krzyki.union(centrum)))


 if len(pozaNFZ) != 0:
     print(pozaNFZ)


#lista = [1, 2, 3, 4, 4, 4, 5, 5, 6]
#lista = list(set(lista))
#print(lista)