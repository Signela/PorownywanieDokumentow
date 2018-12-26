--------------------------------------------------------
--  File created - poniedziałek-grudnia-24-2018   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table TEMAT_DOKUMENTU
--------------------------------------------------------

  CREATE TABLE "C##PPAWLUK"."TEMAT_DOKUMENTU" 
   (	"NAZWA_DOKUMENTU" VARCHAR2(50 BYTE), 
	"TEMATY" VARCHAR2(4000 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into C##PPAWLUK.TEMAT_DOKUMENTU
SET DEFINE OFF;
Insert into C##PPAWLUK.TEMAT_DOKUMENTU (NAZWA_DOKUMENTU,TEMATY) values ('D20181943.txt',' sztandar 3.60%, centymetr 3.18%, rozporządzenie 2.97%, załącznik 2.75%, strona 2.54%, płat 2.33%, kolor 2.33%, sprawa 2.12%, pozycja 2.12%, numer 2.12%,');
Insert into C##PPAWLUK.TEMAT_DOKUMENTU (NAZWA_DOKUMENTU,TEMATY) values ('D20181937.txt',' postępowanie 6.06%, dzień 4.85%, ustawa 4.85%, artykuł 4.24%, karny 3.64%, kodeks 3.64%, pozycja 3.64%, konstytucyjny 3.03%, trybunał 2.42%, tryb 1.82%,');
Insert into C##PPAWLUK.TEMAT_DOKUMENTU (NAZWA_DOKUMENTU,TEMATY) values ('D20181947.txt',' morski 3.09%, hydrograficzny 2.70%, szkolenie 2.38%, hydrograf 2.06%, system 1.51%, praca 1.43%, kategoria 1.43%, dyplom 1.35%, organizacja 1.11%, dana 1.11%,');
Insert into C##PPAWLUK.TEMAT_DOKUMENTU (NAZWA_DOKUMENTU,TEMATY) values ('D20181950.txt',' administracja 3.17%, załącznik 2.82%, wydatek 2.82%, budżet 2.46%, przeniesienie 2.46%, państwo 2.46%, rozporządzenie 2.11%, planować 2.11%, ustawa 2.11%, numer 2.11%,');
