# Hex password generator [a-f,A-F,0-9]
I made this for fun while learning Python. If my 85 year old grandparents can use a password safe with random passwords, you can too.

<rant>
* Use random passwords.
* Use a damn password safe, preferrably one with cloud sync - https://1password.com/ or https://bitwarden.com/
* Check your email addresses against haveibeenpwned - https://haveibeenpwned.com/
* Use strong passwords with lots of characters. Check the stength at sites like - https://howsecureismypassword.net/
</rant>

## Installation
### Requirements
- Python 3

### Usage
```
git clone link
cd to directory
chmod +x pwgen.py
./pwgen.py
```
You'll be asked:
- How many characters do you want the password to be?
- How many passwords do you want?

## Example
```
# root @ devbox in ~/Hex-Password-Generator on git:master x [5:31:38] 
$ ./pwgen.py 

HEX PASSWORD GENERATOR

HOW LONG: 24
HOW MANY: 8
16Fd5ed82BBF5ce6F0caBFEd
43C2BE2D2d2b5eCe78d7aCC9
c4C8005F66DAcBDbD7fB7FC6
dC9CD885AE7ed7a578b1602B
cB4eaC8da3F4C1DCb8fD33F2
3F0A24FD1a2f40E021CcAdaB
2298D7F6EACED06CDDf654aB
A6cFFffa496BBCCCBCbF9cbb
```

# PseudorandomPWs
twitter.com/PseudorandomPWs

# What this is...

This is a quick and dirty python3 script to automatically tweet a random password every x seconds. You will need a twitter api key and installing tweepy (pip3 install tweepy --user) priot to use. You’ll need to enter in the api information within the script, specify the length and quantity of password per tweet, and finally how often they are to be tweeted.
