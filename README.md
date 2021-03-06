# pushm (private user shared memory)

![Language](https://img.shields.io/badge/Language-python3-yellow.svg?style=flat&logo=python)
![Version](https://img.shields.io/github/v/release/jd297/pushm.svg)
[![License](https://img.shields.io/github/license/jd297/pushm.svg)](https://github.com/JD297/pushm/blob/master/LICENSE.md)
![Lastcommit](https://img.shields.io/github/last-commit/jd297/pushm.svg)
![Total lines](https://img.shields.io/tokei/lines/github/jd297/pushm)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/jd297/pushm.svg)](https://github.com/JD297/pushm/issues)

## Introduction
You can put text data into a pushm session and retrieve it later in another command. An example use case could be to build a mysql command with secure credentials. It could get very frustrating to copy always the same password from a password-manager for the same mysql command. With pushm you can store multiple credentials or other data within an encrypted session and use it in commands.

```bash
# Initialize your session with a password
$ pushm --repo database
[pushm] Password for "database": 

# Get your session data in json format
$ pushm --repo database
[pushm] Password for "database": 
{
	"user": "admin",
	"pass": "$ecur3P@ssw0rd"
}

# Insert data into a session by slot name
$ pushm --repo database -s name -i
[pushm] Password for "database": 
[pushm] Data for slot "name": JD297

# Insert data into a session via pipe by slot name
$ cut -d':' -f2 creds.txt | pushm --repo database -s password -p
[pushm] Password for "database": 

# Select data from a session by slot name
$ pushm --repo database -s name
[pushm] Password for "database": 
JD297

# Example:
$ mysql -u $(pushm -r db -s user) -p$(pushm -r db -s pass) -h localhost mydb < backup.sql
[pushm] Password for "db": 
```

Credentials that are in an inline command will not be displayed as plaintext in the shell history.
```bash
$ history
 1000 mysql -u $(pushm -r db -s user) -p$(pushm -r db -s pass) -h localhost mydb < backup.sql
```

## Requirements
You need to install python3 and the module "pycrypto" that are mostly installed by default on linux.

## Install

### Install to /opt and link to /usr/local/bin (recommended)
```bash
$ cd /opt
$ sudo git clone https://github.com/JD297/pushm
$ sudo ln -s $(pwd)/src/pushm /usr/local/bin/
```

### Install to home directory and link to ~/.local/bin (not recommended)
ATTENTION: Your passwords can be fished if other people have write privileges to the pushm directory
```bash
$ cd ~
$ git clone https://github.com/JD297/pushm
$ cd pushm
$ mkdir -p ~/.local/bin
$ ln -s $(pwd)/src/pushm ~/.local/bin/

# Export ~/.locale/bin PATH
# Check if the path already exists
echo $PATH
export PATH=~/.local/bin:$PATH
```

## Sessions
Your session will be saved to the ".pushm" directory that lives in your home directory. All session files will be saved as YOUR_REPO_NAME.session. The session file is encrypted with AES256. The file contains your session data in JSON format.

## Security
Basicly pushm is secured by the [AES256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)-[CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)) and [SHA2](https://en.wikipedia.org/wiki/SHA-2) algoithms. The session directory will be created with the 0700 mask and session files will gets the mode 0600. The password is hashed with the SHA256 alogorithm, so the password has always a 256bit strength. If the session file gets corrupted by an attacker, an exception will be thrown, because the password is wrong and the program exits with code 1 and no data will be returned to the terminal.

## Credits
Special thanks to [@TheMorpheus407](https://github.com/TheMorpheus407/) he has written an easy to use python AES file encryption script.

The source code was completly written in my terminal editor [cedit](https://github.com/jd297/cedit/), so definetly checkout this repository.
