import os
import csv
from operator import itemgetter, attrgetter
words = []
f = open('TFIDF.csv', 'r')
with f:
    csvreader = csv.reader(f, delimiter=';')
    headers = []
    for i in csvreader:
        for j in i:
            headers.append(j)
        break
    headers.remove(headers[0])
    csvreader = csv.reader(f, delimiter=';')
    for i in csvreader:
        words.append(i)
myHeader = ['pliki','słowa']
f = open('WszystkieWspolneTermy.csv', 'w', newline='')
with f:
    fnames = myHeader
    writer = csv.DictWriter(f, fieldnames=fnames,delimiter=';')
    writer.writeheader()
    matrix = []
    tab = {}
    wordTxt = ''
    for i in range(1,len(headers)+1,1):
        myH = headers[i-1];
        terms = []
        tmp = sorted(words,key=lambda k: float(k[i]),reverse=True)
        for j in tmp:
            if(float(j[i])>0.0):
                terms.append(j)
        for h in headers:
            if (myH != h):
                tab.__setitem__('pliki', myH + ',' + h)
                for term in terms:
                    i=0
                    for w in words:
                        for t in term:
                            if(t==w[0] and float(w[headers.index(h)+1])>0.0):
                                i=i+1
                                wordTxt = wordTxt  + w[0] + ' ' + (terms.index(term)+1).__str__() + ', '
                tab.__setitem__('słowa', wordTxt)
                wordTxt = ''
                print(tab)
                if(tab.get('słowa')!=''):
                        writer.writerow(tab)
                tab.clear()
myHeader = ['pliki','słowa']
f = open('WszystkieWspolneTermyBezPowtorzen.csv', 'w', newline='')
with f:
    fnames = myHeader
    writer = csv.DictWriter(f, fieldnames=fnames,delimiter=';')
    writer.writeheader()
    matrix = []
    tab = {}
    wordTxt = ''
    for i in range(1,len(headers)+1,1):
        myH = headers[i-1];
        terms = []
        tmp = sorted(words,key=lambda k: float(k[i]),reverse=True)
        for j in tmp:
            if(float(j[i])>0.0):
                terms.append(j)
        for h in headers:
            if (myH != h and (headers.index(h)+1)>i):
                tab.__setitem__('pliki', myH + ',' + h)
                tmpH = sorted(words,key=lambda k: float(k[headers.index(h)+1]),reverse=True)
                for term in terms:
                    i=0
                    for w in words:
                        for t in term:
                            if(t==w[0] and float(w[headers.index(h)+1])>0.0):
                                i=i+1
                                wordTxt = wordTxt  + w[0] + ' ' + (terms.index(term)+1).__str__() + ';' +(tmpH.index(term)+1).__str__() + ', '
                tab.__setitem__('słowa', wordTxt)
                wordTxt = ''
                print(tab)
                if(tab.get('słowa')!=''):
                        writer.writerow(tab)
                tab.clear()
