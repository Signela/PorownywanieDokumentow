from math import sqrt
import csv
header = []
words = []
odlegloscKontowa = []
odlegloscJaccarda = []
f = open('Macierz.csv', 'r')
with f:
    csvreader = csv.reader(f, delimiter=';')
    for i in csvreader:
        for j in i:
            header.append(j)
        break
    header.remove(header[0])
    next(f)
    csvreader = csv.reader(f, delimiter=';')
    for i in csvreader:
        tab = []
        for j in i:
            tab.append(j)
        word = tab[0]
        tab.remove(word)
        words.append([word,tab])
    sumaIloczynow = []
    sumaKwadratow =[]
    relacjaPlikow = []
    for i in words:
        for j in range(0,i[1].__len__(),1):
            for z in range(j+1,i[1].__len__(), 1):
                sumaIloczynow.append(0)
                relacjaPlikow.append([header[j],header[z]])
            sumaKwadratow.append(0)
        break
    for i in words:
        iterator =0
        for j in range(0,i[1].__len__(),1):
            sumaKwadratow[j] = int(i[1][j]) * int(i[1][j]) + int(sumaKwadratow[j])
            for z in range(j+1, i[1].__len__(), 1):
                sumaIloczynow[iterator] = int(i[1][j])*int(i[1][z])+int(sumaIloczynow[iterator])
                iterator = iterator+1
    pierwiastekIloczynowSumyKwadratow = []
    mianownikJaccarda = []
    for i in words:
        iterator = 0
        for j in range(0, i[1].__len__(), 1):
            for z in range(j + 1, i[1].__len__(), 1):
                pierwiastekIloczynowSumyKwadratow.append(sqrt(sumaKwadratow[j]*sumaKwadratow[z]))
                mianownikJaccarda.append(sumaKwadratow[j]+sumaKwadratow[z]-sumaIloczynow[iterator])
                iterator = iterator + 1
        break
    for i in range(0,relacjaPlikow.__len__(),1):
        odlegloscKontowa.append([relacjaPlikow[i],1-(float(sumaIloczynow[i])/float(pierwiastekIloczynowSumyKwadratow[i]))])
        odlegloscJaccarda.append([relacjaPlikow[i],1-(float(sumaIloczynow[i])/float(mianownikJaccarda[i]))])
    print("odlegloscKontowa")
    for i in odlegloscKontowa:
        print(i)
    print("odlegloscJaccarda")
    for i in odlegloscJaccarda:
        print(i)
odlegloscK = open('OdlegloscK.csv', 'w', newline='')
with odlegloscK:
    fnames = ['Nazwa Pliku'] + header
    writer = csv.DictWriter(odlegloscK, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for file in header:
        tab.__setitem__('Nazwa Pliku',file)
        for odleglosc in odlegloscKontowa:
            if(odleglosc[0][0] == file):
                tab.__setitem__(odleglosc[0][1], odleglosc[1])
            elif (odleglosc[0][1] == file):
                tab.__setitem__(odleglosc[0][0], odleglosc[1])
        writer.writerow(tab)
        tab.clear()
odlegloscJ = open('OdlegloscJ.csv', 'w', newline='')
with odlegloscJ:
    fnames = ['Nazwa Pliku'] + header
    writer = csv.DictWriter(odlegloscJ, fieldnames=fnames, delimiter=';')
    writer.writeheader()
    tab = {}
    for file in header:
        tab.__setitem__('Nazwa Pliku',file)
        for odleglosc in odlegloscJaccarda:
            if(odleglosc[0][0] == file):
                tab.__setitem__(odleglosc[0][1], odleglosc[1])
            elif (odleglosc[0][1] == file):
                tab.__setitem__(odleglosc[0][0], odleglosc[1])
        writer.writerow(tab)
        tab.clear()