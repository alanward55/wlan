# Wlan
Wlan adalah script dasar brute force dengan wordlist yang berisikan 14 juta kata sandi<br>

# Instalasi
```
apt update
apt upgrade -y
apt install python2 -y
apt install iwconfig -y
apt install aircrack-ng -y
apt install git -y
git clone https://github.com/alanward55/wlan
cd wlan
python2 wifi.py
```
## Cara Menggunakan
-> Jalankan script<br>
-> Isikan nama interface adapter wifi anda (paling bawah, biasanya wla0)<br>
-> Tunggu beberapa saat sampai semua wifi terbaca, lalu tekan ctrl+c<br>
-> Salin alamat BSSID nya<br>
-> Tempelkan pada tempatnya<br>
-> Tulis Nomor CH wifi<br>
-> Setelah jendela terminal baru terbuka, salin command yang harus disalin kemudian tempelkan pada jendela baru, kemudian enter<br>
-> Masukkan lokasi untuk menyimpan handshake<br>
	/home = home atau root<br>
	/user = nama user linux kalian<br>
	/folder = nama folder (wifi adalah nama folder bawaan)<br>
	/file = nama file (tanpa menyertakan garis miring "/" diakhir)<br>
-> Contoh: /home/alan/wifi/handshake
-> Enter lalu tunggu hingga handshake ditemukan (wpa handshake found!)<br>
-> Kemudian tekan ctrl+c lalu masukkan lokasi wordlist<br>
-> Lokasi wordlist bawaan adalah /home/user/wifi/worlist.txt<br>
-> /home bisa saja ditukar dengan root<br>
-> /user sesuaikan dengan username linux anda<br>
-> Kemudian tekan enter dan tunggu hingga wordlist menemukan kata sandi yang sesuai<br>

## PENTING!!!
Script tidak akan berjalan baik jika lokasi handshake atau wordlist tidak tepat

# Join
<p align="left">
<a href="https://github.com/alanward55"><img src="https://img.shields.io/badge/GitHub-Follow%20on%20GitHub-inactive.svg?logo=github"></a>
</p><p align="left">

<p align="left">
<a href="https://t.me/terminalnewbe"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>
</p>
# Hubungi Saya
Email : ondeuli@gmail.com<br>
Phone : +6285326728933

# Donasi
Dana : 085326728933<br>
Doge : D7CeRA5VqnAGN7h4iL33N3ywx4pXUCLvWM
