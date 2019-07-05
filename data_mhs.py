from decimal import *
import csv
import string
import random
import time


start = time.time()

#generate Nama random
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#generate Nilai random
def nilaiRan():
    nilai = random.randint(1,100)
    return nilai

#generate NPM random
def NPM():
    random_npm = round(Decimal(random.uniform(500.0,799.9)*10000),0)
    return random_npm

#penulisan data Dummy
with open('Data_mhs.csv', 'w', newline='') as f:
    record_data = csv.writer(f)

    record_data.writerow(['Nomor','Nama','NPM','nilai1','nilai2',
                   'nilai3','nilai4','nilai5','nilai6','nilai7',
                   'nilai8','nilai9','nilai10','nilai11','nilai12',
                   'nilai13','nilai14','nilai15','nilai16','nilai17',
                   'nilai18', 'nilai19', 'nilai20', 'nilai21', 'nilai22',
                   'nilai23', 'nilai24'])

    for x in range (1,1000001):
        record_data.writerow([x, randomString(), NPM(), nilaiRan(),
                   nilaiRan(),nilaiRan(),nilaiRan(),nilaiRan(),nilaiRan(),
                   nilaiRan(),nilaiRan(),nilaiRan(),nilaiRan(),nilaiRan(),
                   nilaiRan(),nilaiRan(),nilaiRan(),nilaiRan(),nilaiRan(),
                   nilaiRan(), nilaiRan(), nilaiRan(), nilaiRan(), nilaiRan(),
                   nilaiRan(), nilaiRan(), nilaiRan()])

end = time.time()
dur = end-start

if dur<60:
    print("Execution Time:",dur,"seconds")
elif dur>60 and dur<3600:
    dur=dur/60
    print("Execution Time:",dur,"minutes")
else:
    dur=dur/(60*60)
    print("Execution Time:",dur,"hours")
