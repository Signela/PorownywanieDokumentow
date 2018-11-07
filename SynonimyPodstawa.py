import cx_Oracle
import os
import io

os.environ["NLS_LANG"] = "POLISH_POLAND.AL32UTF8"
connection = cx_Oracle.connect("C##PPAWLUK", "#Lex2018", "144.21.89.60:1521/ORCL.591263988.oraclecloud.internal")
cur = connection.cursor()
cur1 = connection.cursor()
cur2 = connection.cursor()
cur3 = connection.cursor()
slownik_synonimow = cur.execute('select * from SYNONIMY_ORGINALNE');
naglowki = ['slowo_podstawowe', 'synonim1', 'synonim2', 'synonim3', 'synonim4', 'synonim5', 'synonim6', 'synonim7',
            'synonim8', 'synonim9', 'synonim10', 'synonim11', 'synonim12', 'synonim13', 'synonim14', 'synonim15', 'synonim16',
            'synonim17', 'synonim18', ]
for slowo in slownik_synonimow:
    i = 0
    for s in slowo:
        slownikPolskiego = cur1.execute(
            'select SLOW_FORMA_PODSTAWOWA from SLOWNIK where SLOW_WYRAZ = \'{}\' and rownum = 1'.format(s));
        for word in slownikPolskiego:
            print("Zmieniam {} na {} przy naglowku {}".format(s,word[0],naglowki[i]))
            cur2.execute('UPDATE synonimy_orginalne set {} = \'{}\' where {} = \'{}\''.format(naglowki[i],word[0],naglowki[i],s))
            cur2.execute('commit')
        i = i+1
cur.execute('commit')
cur1.execute('commit')
cur3.execute('commit')
cur.close()
cur1.close()
cur2.close()
cur3.close()
connection.close()
