import subprocess
import json
import webbrowser

txid = input("Enter Certificate Id: ")
rawtx = subprocess.check_output(["flo-cli", "getrawtransaction", str(txid)])
rawtx = str(rawtx)
rawtx = rawtx[2:-3]

tx = subprocess.check_output(["flo-cli",, "decoderawtransaction", str(rawtx)])
content = json.loads(tx)
page_html = content['floData']

signature = page_html[0:88]
page_html = page_html[88:]

issued_by = input("Enter address of the issuing authority: ")
status = subprocess.check_output(["flo-cli","verifymessage",issued_by,signature,str(page_html)])
status = str(status)
status = status[2:-3]

if(status=='true'):
	print("Certificate verification successfull.")
	cert = open("./certificates/"+txid+".html",'w')
	cert.write(page_html)
	url = "./certificates/"+txid+".html"
	webbrowser.open_new(url)
else:
	print('The certificate is invalid.')

