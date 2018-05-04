import sys
import zipfile
import os
import shutil

src = "C:\\Users\\KasturiC\\Anaconda3\\emovoice-master\\data\\chunks\\download.zip"
dst = "C:\\Users\\KasturiC\\Anaconda3\\emovoice-master\\data\\chunks"

if not os.path.exists(dst + '\\tmp\\'):
    os.mkdir(dst + '\\tmp\\')

print ('unpacking ' + src + '...')

zip_ref = zipfile.ZipFile(src, 'r')
zip_ref.extractall(dst + '\\tmp\\')
zip_ref.close()

print ('done')

print ('creating folders...')

emos = {  'W' : 'anger', 
          'L' : 'boredom', 
          'E' : 'disgust',
          'A' : 'fear',
          'F' : 'happiness',
          'T' : 'sadness',
          'N' : 'neutral'  }

for key, value in emos.items():
    name = dst + '\\' + value
    if not os.path.exists(name):
        os.mkdir(name)

print ('done')

print ('copy files...')

for root, dirs, files in os.walk(dst + '\\tmp\\wav'):
    for file in files:
        emo = file[5]
        srcFile = root + '\\' + file
        dstFile = dst + '\\' + emos[emo] + '\\' + file        
        shutil.copy(srcFile, dstFile)

print ('done')

print ('removing temporary files...')

shutil.rmtree(dst + '\\tmp\\')

print ('done')
