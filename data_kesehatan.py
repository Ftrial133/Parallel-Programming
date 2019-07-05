from decimal import *
import csv
import string
import random
import time

start = time.time()

#generate Nama random
def randomNama(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#fungsi generate Alamat random
def randomAlamat(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#fungsi generate Y atau T
def ind_YT():
    indikator = ''
    hasil = random.randint(1,10)
    if hasil % 2 == 0:
        indikator = 'Y'
    elif hasil % 2 == 1:
        indikator = 'T'
    return indikator
    return hasil


#penulisan data Dummy
with open('Data_kesehatan.csv', 'w', newline='') as f:
    record_data = csv.writer(f)

    record_data.writerow(['Nomor','Nama','Alamat','indikator1','indikator2',
                   'indikator3','indikator4','indikator5','indikator6','indikator7',
                   'indikator8','indikator9','indikator10','indikator11','indikator12'])

    for x in range (1,1000001):
        record_data.writerow([x, randomNama(), 'Jl.' + randomAlamat(), ind_YT(), ind_YT(),
                   ind_YT(),ind_YT(),ind_YT(),ind_YT(),ind_YT(),
                   ind_YT(),ind_YT(),ind_YT(),ind_YT(),ind_YT()])


end = time.time()
dur = end-start

if dur<60:
    print("Execution Time:",dur,"seconds")
elif dur>60 and dur<3600:
    durm = round(dur/60, 0)
    durs = (dur*60)-3600
    print("Execution Time:",durm,"minutes",durs,"seconds")
else:
    dur=dur/(60*60)
    print("Execution Time:",dur,"hours")
