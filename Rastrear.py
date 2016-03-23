import urllib2, json, sys
#Variaveis
URL = "http://ip-api.com/json/" + sys.argv[1] + "?fields=258047"
API = urllib2.urlopen(URL)
data = json.loads(API.read())

def g(var):
	return data[var]

print "Pais: " + g("country") + "(" + g("countryCode") + ")\n" + "Regiao: " + g("regionName") + "\nCidade: " + g("city") + "\nISP: " + g("isp") + "\nTimeZone: " + g("timezone") + "\nOrganizacao: " + g("org") + "\nAS: " + g("as") + "\nCodigo-Postal(Zip): " + g("zip") + "\n  Develop by gusd"
