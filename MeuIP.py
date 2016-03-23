import urllib2

MeuIP = urllib2.urlopen("https://api.ipify.org")

print MeuIP.read()

