--------------------------------------------------------
--  File created - wtorek-stycznia-08-2019   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table TEMAT_DOKUMENTU
--------------------------------------------------------

  CREATE TABLE "SYSTEM"."TEMAT_DOKUMENTU" 
   (	"NAZWA_DOKUMENTU" VARCHAR2(50 BYTE), 
	"TEMATY" VARCHAR2(4000 BYTE)
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into SYSTEM.TEMAT_DOKUMENTU
SET DEFINE OFF;
Insert into SYSTEM.TEMAT_DOKUMENTU (NAZWA_DOKUMENTU,TEMATY) values ('D20181943.txt',' sztandar 3.56%, centymetr 3.14%, rozporz¹dzenie 2.93%, za³¹cznik 2.51%, strona 2.51%, p³at 2.30%, sprawa 2.09%, pozycja 2.09%, numer 2.09%, pañstwowy 1.88%, wat 1.88%, minister 1.46%, wewnêtrzny 1.46%, jednostka 1.46%, dzieñ 1.46%,');
Insert into SYSTEM.TEMAT_DOKUMENTU (NAZWA_DOKUMENTU,TEMATY) values ('D20181937.txt',' postêpowanie 5.45%, dzieñ 4.85%, ustawa 4.85%, arta 4.24%, kodeks 3.64%, karny 3.64%, pozycja 3.64%, konstytucyjny 3.03%, trybuna³ 2.42%, zakres 1.82%, punkt 1.82%, jêdrzejewski 1.82%, podstawa 1.82%, kieres 1.82%, tryba 1.82%,');
Insert into SYSTEM.TEMAT_DOKUMENTU (NAZWA_DOKUMENTU,TEMATY) values ('D20181947.txt',' morski 3.16%, hydrograficzny 2.69%, szkolenie 2.37%, hydrograf 2.06%, system 1.50%, praca 1.42%, kategoria 1.42%, dyplom 1.34%, organizacja 1.11%, dana 1.11%, ustawa 1.11%, pomiar 1.03%, numer 1.03%, szef 0.95%, pozycja 0.95%,');
Insert into SYSTEM.TEMAT_DOKUMENTU (NAZWA_DOKUMENTU,TEMATY) values ('D20181950.txt',' wynagrodzenie 3.51%, administracja 3.16%, za³¹cznik 2.81%, wydatek 2.81%, pañstwo 2.46%, bud¿et 2.46%, przeniesienie 2.46%, planowaæ 2.11%, rozporz¹dzenie 2.11%, numer 2.11%, kwota 2.11%, ustawa 2.11%, czêsty 1.75%, przestrzenny 1.75%, dzieñ 1.75%,');
