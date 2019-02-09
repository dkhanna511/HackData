import urllib.request as urllib2

filedata = urllib2.urlopen('https://firebasestorage.googleapis.com/v0/b/agriculture-baf5b.appspot.com/o/images%2F6b7948c1-76a7-45a2-8924-3a80db3c2410?alt=media&token=b7fd79c6-abe4-4ffc-9396-1ea90e8d14a6')  
datatowrite = filedata.read()

with open('sample.jpg', 'wb') as f:  
    f.write(datatowrite)
