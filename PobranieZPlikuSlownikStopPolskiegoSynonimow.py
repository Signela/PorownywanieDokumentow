import cx_Oracle
import os
import PyPDF3
import io

os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
connection = cx_Oracle.connect("C##PPAWLUK", "#Lex2018", "144.21.89.60:1521/ORCL.591263988.oraclecloud.internal")
cur = connection.cursor()
cur.execute('DELETE FROM "C##PPAWLUK"."DOKUMENT"')
cur.execute('commit')
nameDocuments = os.listdir("dokumenty")
cur.execute('commit')


def pdfparser(data, nr):
    # pdfFileObj = open(data, 'rb')
    # pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
    # print(pdfReader.numPages)
    # print(pdfReader)
    # for i in range(0,pdfReader.numPages,1):
    #     print(pdfReader.getPage(i).extractText())
    file = io.open(data, mode="r", encoding='utf-8-sig')
    myfile = file.read()
    myfile = myfile.lower()
    myfile = myfile.replace('\n', ' ').replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('/',
                                                                                                                   '').replace(
        '\\', '').replace(';', '').replace('"', ' ').replace('\'',' ').replace(']', '').replace('[', '').replace(')', '').replace('(',
                                                                                                               '').replace(
        ':', '').replace('`', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace(
        '^', '').replace('&', '').replace('*', '').replace('-', ' ').replace('_', ' ').replace('+', ' ').replace('=',
                                                                                                                 ' ').replace(
        '0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6',
                                                                                                              '').replace(
        '7', '').replace('8', '').replace('9', '').replace('>', ' ').replace('<', ' ').replace('{', '').replace('}',
                                                                                                                '').replace(
        '§', '').replace('', '').replace('\\ufeff', '').replace(' ', ' ').replace('–', ' ').replace('“', '').replace(
        '„', '').replace('…', '').replace('	', '').replace('’', ' ').replace('”', '').replace('  ', ' ').replace(
        '  ', ' ')
    myfile = myfile.split(' ')
    replaceFile = myfile
    print(replaceFile)
    stopwords = cur.execute('select * from stopwords')
    for word in stopwords:
        while (word[0] in replaceFile):
            replaceFile.remove(word[0])
    removeTab = {'	', '\n', ''}
    for remove in removeTab:
        while (remove in replaceFile):
            replaceFile.remove(remove)
    j = 0
    for word in replaceFile:
        dictionary = cur.execute(
            'select slow_forma_podstawowa from slownik where slow_wyraz = \'{}\' and slow_wyraz != slow_forma_podstawowa and rownum=1'.format(word))
        for i in dictionary:
            replaceFile.__setitem__(j, i[0])
            j = j + 1
    j = 0
    for word in replaceFile:
        thesaurus = cur.execute(
            'select slow_forma_podstawowa from slownik_synonimow where slow_wyraz = \'{}\' and slow_wyraz != slow_forma_podstawowa and rownum=1 '.format(
                word))
        for i in thesaurus:
            replaceFile.__setitem__(j, i[0])
            print(i[0], word)
            j = j + 1
    txt = ''
    for i in range(0, len(replaceFile), 1):
        txt = txt + ' ' + (replaceFile.__getitem__(i))
        if i % 200 == 0 and i != 0:
            cur.execute(
                'INSERT INTO "C##PPAWLUK"."DOKUMENT" (NAZWA_DOKUMENTU, TEKST) VALUES( \'{}\', \'{}\')'.format(
                    nameDocuments[nr], txt))
            cur.execute('commit')
            txt = ''
    if (txt != ''):
        cur.execute(
            'INSERT INTO "C##PPAWLUK"."DOKUMENT" (NAZWA_DOKUMENTU, TEKST) VALUES( \'{}\', \'{}\')'.format(
                nameDocuments[nr], txt))
        cur.execute('commit')
    # cur.execute(
    #     'INSERT INTO "C##PPAWLUK"."DOKUMENT" (NAZWA_DOKUMENTU, TEKST) VALUES( \'{}\', \'{}\')'.format(nameDocuments[nr], myfile))


for i in range(0, len(nameDocuments), 1):
    pdfparser("D:\BSpy\!materiały na studia\Praca inżynierska\Implementacja\PorownywanieDokumentow\dokumenty\{}".format(
        nameDocuments[i]), i)
cur.close()
connection.close()
