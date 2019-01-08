import os
import csv
from operator import itemgetter, attrgetter
terms = []
f = open('TFIDF_TERMY.csv', 'r')
with f:
    csvreader = csv.reader(f, delimiter=';')
    next(f)
    for i in csvreader:
        terms.append(i)
for j in terms:
    print(j)
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
myHeader = ['pliki']
for i in range(1,16,1):
    myHeader.append('słowo'+' '+str(i))
f = open('WspolneTermy.csv', 'w', newline='')
with f:
    fnames = myHeader
    writer = csv.DictWriter(f, fieldnames=fnames,delimiter=';')
    writer.writeheader()
    matrix = []
    tab = {}
    for term in terms:
        for h in headers:
            if(term[0]!=h):
                tab.__setitem__('pliki',term[0]+','+h)
                i=0
                for w in words:
                    for t in term:
                        if(t==w[0] and float(w[headers.index(h)+1])>0.0):
                            print("w to ",w[0]," t to ",t," wartosc w to ",w[headers.index(h)+1])
                            i=i+1
                            tab.__setitem__('słowo'+' '+str(i),w[0])
                print(tab)
                if(len(tab)!=1):
                    writer.writerow(tab)
                tab.clear()
words = []
write = []
writes = []
f = open('WspolneTermy.csv', 'r')
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
    for w1 in words:
        flag = True
        for w2 in words:
            tab1 = w1[0].split(',')
            tab2 = w2[0].split(',')
            if(tab1[0]==tab2[1] and tab1[1]==tab2[0]):
                flag = False
                write.append(w1[0])
                for w in w1:
                    if(w!= w1[0]):
                        write.append(w)
                for w in w2:
                    if(w!= w2[0] and (w not in write)):
                        if '' in write:
                            write.__setitem__(write.index(''),w)
                        else:
                            write.append(w)
        if(flag==False):
            tab1 = write[0].split(',')
            flag2=True
            for k in writes:
                k1 = k[0].split(',')
                if((k1[0]==tab1[0] and k1[1]==tab1[1]) or (k1[0]==tab1[1] and k1[1]==tab1[0])):
                    print("k ",k1," tab1 ",tab1," tab2 ",tab2)
                    flag2=False
            if(flag2):
                writes.append(write)
        else:
            writes.append(w1)
        write = []
for w in writes:
    print(w)          
myHeader = ['pliki']
for i in range(1,31,1):
    myHeader.append('słowo'+' '+str(i))
f = open('WspolneTermyBezPowtorzen.csv', 'w', newline='')
with f:
    fnames = myHeader
    writer = csv.DictWriter(f, fieldnames=fnames,delimiter=';')
    writer.writeheader()
    matrix = []
    tab = {}
    for term in writes:
        tab.__setitem__('pliki',term[0])
        for i in range(1,len(term),1):
            tab.__setitem__('słowo'+' '+str(i),term[i])
        print(tab)
        writer.writerow(tab)
        tab.clear()
