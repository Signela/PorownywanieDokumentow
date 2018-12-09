from math import sqrt

import cx_Oracle
import os
import csv
from operator import itemgetter, attrgetter
f = open('Macierz.csv', 'r')
header = []
words = []
with f:
    csvreader = csv.reader(f, delimiter=';')
    for i in csvreader:
        for j in i:
            header.append(j)
        break
    header.remove(header[0])
    print(header)
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
    print(sumaIloczynow.__len__())
    for i in words:
        iterator =0
        for j in range(0,i[1].__len__(),1):
            sumaKwadratow[j] = int(i[1][j]) * int(i[1][j]) + int(sumaKwadratow[j])
            for z in range(j+1, i[1].__len__(), 1):
                sumaIloczynow[iterator] = int(i[1][j])*int(i[1][z])+int(sumaIloczynow[iterator])
                iterator = iterator+1
    print(sumaIloczynow)
    print(sumaKwadratow)
    pierwiastekIloczynowSumyKwadratow = []
    for i in words:
        iterator = 0
        for j in range(0, i[1].__len__(), 1):
            for z in range(j + 1, i[1].__len__(), 1):
                pierwiastekIloczynowSumyKwadratow.append(sqrt(sumaKwadratow[j]*sumaKwadratow[z]))
        break
    print(pierwiastekIloczynowSumyKwadratow)
    print(relacjaPlikow)
    odlegloscKontowa = []
    for i in range(0,relacjaPlikow.__len__(),1):
        odlegloscKontowa.append([relacjaPlikow[i],(float(sumaIloczynow[i])/float(pierwiastekIloczynowSumyKwadratow[i]))])
    print(odlegloscKontowa)

