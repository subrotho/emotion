import os
import sys
import ntpath

rootdir = "C:\\Users\\KasturiC\\Anaconda3\\emovoice-master\\"

fp = open(rootdir + 'list.txt', 'w')

print(fp)

for root, subdirs, files in os.walk(rootdir):
    for file in files:      
        name, ext = os.path.splitext(file)
        if ext.lower() == '.wav':
            print(root + '\\' + file)        
            path = root + '\\' + file
            print(path)
            label = ntpath.basename(root)
            print(label)
            fp.write(path + ';' + label + '\n')

fp.close()
        