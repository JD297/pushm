import json
import os
from aes import encrypt
from aes import decrypt

homedir = os.path.expanduser("~")
basedir = os.path.join(homedir, ".pushm")

def check_basedir():
	return os.path.isdir(basedir)

def create_basedir():
	os.mkdir(basedir)

def check_session(session_file):
	return os.path.isfile(session_file)

def create_session(session_file, password, data):
	encrypt(session_file, password, data)

def get_json_session(session_file, password):
	data = decrypt(session_file, password)

	return json.loads(data)

def print_session(session_file, password):
	sdata = get_json_session(session_file, password)

	print(json.dumps(sdata, indent=4))

def handle_repo(name, password):
	session_file = os.path.join(basedir, name + ".session")

	if not check_basedir():
		create_basedir()

	if not check_session(session_file):
		create_session(session_file, password, "{}")
	else:
		print_session(session_file, password)

def handle_select(name, password, key):
	session_file = os.path.join(basedir, name + ".session")

	sdata = get_json_session(session_file, password)

	print(sdata[key])

def handle_insert(name, password, key, data):
	session_file = os.path.join(basedir, name + ".session")

	sdata = get_json_session(session_file, password)

	sdata[key] = data

	create_session(session_file, password, json.dumps(sdata, indent=4))
