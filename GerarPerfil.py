import urllib2, json, sys, io
#Variaveis
URL = "https://randomuser.me/api/index.php?nat=BR"
API = urllib2.urlopen(URL)
data = json.loads(API.read())
URL2 = "http://geradorapp.com/api/v1/"
APICPF = urllib2.urlopen(URL2 + "cpf/generate?token=aafe3b877bf4a79ed7701901e45f43ed")
dataCPF = json.loads(APICPF.read())
APICPNJ = urllib2.urlopen(URL2 + "cnpj/generate?token=aafe3b877bf4a79ed7701901e45f43ed")
dataCPNJ = json.loads(APICPNJ.read())

def RetornaSub(key1, key2):
	return data["results"][0]["user"][key1][key2]

def Retorna(key):
	return data["results"][0]["user"][key]

print "Nome: " +  data["results"][0]["user"]["name"]["first"] + " " + data["results"][0]["user"]["name"]["last"]
print "Genero: " + Retorna("gender")
print "Endereco: " + RetornaSub("location", "street")
print "Cidade: " + RetornaSub("location", "city")
print "Estado: " + RetornaSub("location", "state")
print "Email: http://www.emailtemporariolivre.com.br/#/armyspy.com/" + RetornaSub("name", "last")
print "Usuario: " + Retorna("username")
print "Senha: " + Retorna("password")
print "Telefone: " + Retorna("phone")
print "Telefone2: " + Retorna("cell")
print "CPF: " + dataCPF["data"]["number"] + " (" + dataCPF["data"]["number_formated"] + ")"
print "CPNJ: "+ dataCPNJ["data"]["number"] + " (" + dataCPNJ["data"]["number_formated"] + ")"
print "\n \n Gerado by gusd Tool"
if(len(sys.argv) > 2):
	if(sys.argv[1] == "-s"):
		if(len(sys.argv[2]) > 0):
			file = open(sys.argv[2], "w")
			file.write("Nome: " +  data["results"][0]["user"]["name"]["first"] + " " + data["results"][0]["user"]["name"]["last"] + "\n")
			file.write("Genero: " + Retorna("gender")+ "\n")
			file.write("Endereco: " + RetornaSub("location", "street")+ "\n")
			file.write("Cidade: " + RetornaSub("location", "city")+ "\n")
			file.write("Estado: " + RetornaSub("location", "state")+ "\n")
			file.write("Email: http://www.emailtemporariolivre.com.br/#/armyspy.com/" + RetornaSub("name", "last")+ "\n")
			file.write("Usuario: " + Retorna("username")+ "\n")
			file.write("Senha: " + Retorna("password")+ "\n")
			file.write("Telefone: " + Retorna("phone")+ "\n")
			file.write("Telefone2: " + Retorna("cell")+ "\n")
			file.write("CPF: " + dataCPF["data"]["number"] + " (" + dataCPF["data"]["number_formated"] + ")" + "\n")
			file.write("CPNJ: "+ dataCPNJ["data"]["number"] + " (" + dataCPNJ["data"]["number_formated"] + ")" + "\n")
			file.write("\n \n Gerado by gusd Tool\n")
			file.close()
			print "Salvo com sucesso! \n"

print "\n\nvlws flws\n\n"




