# Recover passwords
[]: # License: MIT

A docker file in ubuntu, so we can easily recover passwords.

# John the Ripper examples
john --wordlist=/var/passwords/wordlists/jonh-password.txt --fork=3 /var/passwords/passwords.shadow

john --wordlist=/var/passwords/wordlists/amass/all.txt --fork=3 /var/passwords/new_to_crack.txt

# Hashcat examples

hashcat -m 500 --username -O -a 6 /var/passwords/new_to_crack.txt /var/passwords/wordlists/jonh-password.txt ?d?d?d

hashcat -m 500 --username -O -a 6 /var/passwords/new_to_crack.txt /var/passwords/wordlists/jonh-password.txt ?d?d?d

hashcat -m 500 results.txt --username -O -a 3 /var/passwords/new_to_crack.txt /var/passwords/wordlists/rockyou.txt ?d?d?d

# Help
- hashcat -I
- [hashcat cheatsheet](https://cheatsheet.haax.fr/passcracking-hashfiles/hashcat_cheatsheet/)