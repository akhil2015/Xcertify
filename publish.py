import re
import subprocess
import htmlmin
template=open("html/index.html", "r")
page_html=template.read()
page_html = htmlmin.minify(page_html, remove_empty_space=True)
print("Loaded Default Theme.")
#regex for identifying attributes
exp =r"{{\w+}}"
attributes  = re.findall(exp,page_html)
r_attributes = attributes[:]
print()
print("Detected following attributes")
#removing curly brackets from attribute
for i in range(0,len(attributes)):
	attributes[i] = attributes[i][2:-2]
	print(str(i+1)+". "+attributes[i])

values=[]
print("Input Values for new certificate");
for i in range(0,len(attributes)):
	inp = input(attributes[i]+" : ")
	values.append(inp)

#replacing values in the code
for i in range(0,len(values)):
	page_html = page_html.replace(r_attributes[i],values[i])

print(len(page_html))

receiver = input("Enter Receiver's Address: ")

#signing the certificate
sender = input("Enter your Address(for signing the certificate): ")
signature = subprocess.check_output(["flo-cli","signmessage",sender,str(page_html)])
signature = str(signature)
signature = signature[2:-3]
print(len(signature))
page_html = signature+page_html

#writing the certificate on the blockchain
txid = subprocess.check_output(["flo-cli", "sendtoaddress",receiver,"0.01",'""','""',"true","false","10",'UNSET',str(page_html)])
txid = str(txid)
txid = txid[2:-3]
print("Certificate Successfully Generated: "+txid)
