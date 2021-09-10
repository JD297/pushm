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

def encrypt(file_path, password, data):
	key = get_key(password)

	file_size = str(len(data)).zfill(16)

	IV = Random.new().read(16)
	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(file_path, 'wb') as f_output:
		f_output.write(file_size.encode('utf-8'))
		f_output.write(IV)

		chunk_pos = 0

		while True:
			chunk = bytes(data[chunk_pos:chunks], "utf-8")

			if len(chunk) == 0:
				break

			if len(chunk) % 16 != 0:
				chunk += b' ' * (16 - (len(chunk) % 16))
				chunk_pos += chunks

			f_output.write(encryptor.encrypt(chunk))

def decrypt(file_path, password):
	key = get_key(password)

	data = ""

	with open(file_path, 'rb') as f_input:
		filesize = int(f_input.read(16))
		IV = f_input.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, IV)

		while True:
			chunk = f_input.read(chunks)

			if len(chunk) == 0:
				break

			data += decryptor.decrypt(chunk).decode("utf-8")[:filesize]

		return data

def get_key(password):
	hashing = SHA256.new(password.encode('utf-8'))
	return hashing.digest()




