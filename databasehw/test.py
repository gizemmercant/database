import sqlite3
import csv

veritabani = sqlite3.connect("kisiler.sqlite3")
imlec = veritabani.cursor()



with open('kisiler.txt', 'r') as fin:
  dr = csv.DictReader(fin)
  kisi = [(i['ISIM'], i['DOWN'], i['UP']) for i in dr]
  print(kisi)


def tablo_olustur():
  komut = ("CREATE TABLE IF NOT EXISTS kisiler(isim TEXT, dowloadmiktari INT NOT NULL,uploadmiktari INT NOT NULL)")
  imlec.execute(komut)

def bilgi_ekle():
  imlec.executemany("INSERT INTO kisiler VALUES (?,?,?);", kisi)
  veritabani.commit()

def verileri_yazdir():
  komut = ("SELECT * FROM kisiler")
  imlec.execute(komut)
  liste = imlec.fetchall()
  print("Kisiler tablosunun bilgileri...")
  for i in liste:
    print(i)



tablo_olustur()

bilgi_ekle()

verileri_yazdir()

veritabani.close()