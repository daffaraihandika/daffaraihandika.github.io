# Import package requests dan BeautifulSoup
import requests
from bs4 import BeautifulSoup

#Request ke website
page = requests.get("https://republika.co.id/")

#Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, 'html.parser')

print('Menampilkan objek html')
print('=======================')
print(obj)

print('\nMenampilkan title browser dengan tag')
print('======================================')
print(obj.title)

print('\nMenampilkan title browser tanpa tag')
print('=====================================')
print(obj.title.text)

print('\nMenampilkan semua tag h2')
print('=====================================')
print(obj.find_all('h2'))

print('\nMenampilkan semua teks h2')
print('=====================================')
for headline in obj.find_all('h2'):
    print(headline.text)

print('\nMenampilkan headline berdasarkan div classs')
print('================================================')
print(obj.find_all('div',class_='bungkus_txt_headline_center'))

print('\nMenampilkan semua teks headline')
print('===================================')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    print(headline.find('h2').text)

print('\nMenampilkan headline pada file text')
print('=====================================')
f=open('D:\Tugas Proyek\headline.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
    f.write(headline.find('h2').text)
    f.write('\n')
f.close()


# Import package json
import json
from datetime import datetime
# Deklarasi list kosong
data=[]
now = datetime.now()
# Lokasi file json
f = open('D:\Tugas Proyek\headline.json', 'w')

# dump list dictionary menjadi json
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"Judul":publish.find('h2').text,
                 "Kategori":publish.find('a').text,
                 "WaktuPublish":publish.find('div',class_='date').text,
                 "WaktuScrapping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps=json.dumps(data)
f.writelines(jdumps)
f.close()