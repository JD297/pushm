# Special thanks to:
#   @TheMorpheus407 https://github.com/TheMorpheus407/ (github)
#                   https://www.youtube.com/user/TheMorpheus407 (youtube)
#
# This file was modified by @JD297 look at the orignal sourcecode from @TheMorpheus407:
# https://github.com/TheMorpheus407/Python-Lets-Code/blob/master/EncryptFiles.py
#
#
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

chunks = 32 * 1024

# todo
# encrypt input into session-file (maybe an encrypted json file)
def encrypt(key, filename):
	out_file_name = "encrypted-" + os.path.basename(filename)
	file_size = str(os.path.getsize(filename)).zfill(16) # 0000000000032001
	IV = Random.new().read(16)
	encryptor = AES.new(key, AES.MODE_CFB, IV)
	with open(filename, 'rb') as f_input:
		with open(out_file_name, 'wb') as f_output:
			f_output.write(file_size.encode('utf-8'))
			f_output.write(IV)
			while True:
				chunk = f_input.read(chunks)
				if len(chunk) == 0:
					break
				if len(chunk) % 16 != 0:
					chunk += b' ' * (16 - (len(chunk) % 16))
				f_output.write(encryptor.encrypt(chunk))

# todo
# decrypt session-file into variable (from json to: list or map)
def decrypt(key, filename):
	out_file_name = filename.split("-")[-1]
	with open(filename, 'rb') as f_input:
		filesize = int(f_input.read(16))
		IV = f_input.read(16)
		decryptor = AES.new(key, AES.MODE_CFB, IV)
		with open(out_file_name, 'wb') as f_output:
			while True:
				chunk = f_input.read(chunks)
				if len(chunk) == 0:
					break
				f_output.write(decryptor.decrypt(chunk))
				f_output.truncate(filesize)

def get_key(password):
	hashing = SHA256.new(password.encode('utf-8'))
	return hashing.digest()




