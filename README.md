# pushm (private user shared memory)

## Introduction
You can pipe text data in pushm and retrieve it later in another command. This is very handy e.g. when you need to build a mysql command with credentials but the password is very complex. A single credential could be copied to clipboard. But what is if you need also a credentials with username, password and host for mysql or other services? With pushm you can store temporarily multiple clipboards within an encrypted session and use it in commands. So you only need to prepare your session with your needed credentials and use commands with your set password and get a sudo like password prompt.

```bash
# prepare your seesion with a password
$ pushm --new
[pushm] Password for JD297: ********

# grep, awk or cut your text out of your environment file and pipe it to pushm
$ cut -d':' -f2 creds.txt | pushm --slot DBPASS_JD

# or you get an promot for data (for passwords that are in your password manager)
$ pushm --slot DBUSER_JD
[pushm] Data: JD297

# example use case:
$ mysql -u $(pushm DBUSER_JD) -p$(pushm DBPASS_JD) -h $(pushm DBHOST_JD) $(pushm DBNAME_JD) < backup.sql
[pushm] Password for JD297: ********
```

Also nice is that your credentials that are in an inline command will not be displayed as plaintext in the shell history.
```bash
$ history
 1000 mysql -u $(pushm DBUSER_JD) -p$(pushm DBPASS_JD) -h $(pushm DBHOST_JD) $(pushm DBNAME_JD) < backup.sql
```

So you can also arrow up, hit return, type your password and you can use this command again. So you must not copy the credentials again and again and again (especially when you copy often things to your clipboard that you need to work with this comes very handy).

# Requirements
You need to have python3 installed on your box. Python modules that are required are mostly installed by default on linux and mac.

## Install
```bash
$ git clone https://github.com/JD297/pushm
$ cd pushm
```

### Install to /usr/local/bin
```bash
$ sudo cp src/pushm /usr/local/bin
```

### Install to home directory
```bash
$ mkdir -p ~/.local/bin
$ copy src/pushm ~/.local/bin

# to just type 'pushm' you should export it in your .shellrc file e.g.: ~/.bashrc
# check if PATH is already set
echo $PATH
# if it is not set export the path
export PATH=~/.local/bin:$PATH
```

## Security
Basicly pushm will be secured by the [AES256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)-[CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)) algoithm. Advises for security and how it works against manipulation are following soon to release of version 1.0.0.
