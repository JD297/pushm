# pushm (private user shared memory)

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
You need to have python3 installed on your box. Python modules that are required are mostly installed by default on linux and mac.

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

## Security
Basicly pushm will be secured by the [AES256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)-[CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)) and [SHA2](https://en.wikipedia.org/wiki/SHA-2) algoithms. Advises for security and how it works against manipulation are following soon to release of version 1.0.0.
