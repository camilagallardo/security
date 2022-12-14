# Recover passwords
[]: # License: MIT

A docker file in ubuntu, so we can easily recover passwords.

# John the Ripper examples
- john --wordlist=/var/passwords/wordlists/jonh-password.txt --fork=3 /var/passwords/passwords.shadow

- john --wordlist=/var/passwords/wordlists/amass/all.txt --fork=3 /var/passwords/new_to_crack.txt

# Hashcat examples

- hashcat -m 500 --username -O -a 6 /var/passwords/new_to_crack.txt /var/passwords/wordlists/jonh-password.txt ?d?d?d

- hashcat -m 500 --username -O -a 6 /var/passwords/new_to_crack.txt /var/passwords/wordlists/jonh-password.txt ?d?d?d

- hashcat -m 500 results.txt --username -O -a 3 /var/passwords/new_to_crack.txt /var/passwords/wordlists/rockyou.txt ?d?d?d

- hashcat -a 6 -w4 -m 500 -O --username --opencl-device-types="1,2" -o results.txt "-1?l?u?s?d" new_to_crack.txt passwords/wordlists/rockyou.txt "?s"

# Mass Attack
- hashcat -a 3 -w4 -m 500 -O --username --opencl-device-types="1,2" -o results.txt "-1?l?u?d" new_to_crack.txt  "?u?l?l?l?l19?d?d"
- hashcat -a 3 -w4 -m 500 -O --username --opencl-device-types="1,2" -o results.txt "-1?l?u?d" new_to_crack.txt  '?u?l?l?l?l?l?d'
- hashcat -a 3 -w4 -m 500 -O --username --opencl-device-types="1,2" -o results.txt "-1?l?u?d" new_to_crack.txt  '?u?l?l?l?l?l?d?d'
- hashcat -a 3 -w4 -m 500 -O --username --opencl-device-types="1,2" -o results.txt "-1?l?u?d" new_to_crack.txt  '?u?l?l?l?l?l?d?d?d'
- hashcat -a 3 -w4 -m 500 -O --username --opencl-device-types="1,2" -o results.txt new_to_crack.txt '-1?u?l?d' '?1?1?1?1'
- hashcat -a 6 -w4 -m 500 -O --username -i --opencl-device-types="1,2" -o results.txt new_to_crack.txt wordlists/words.txt '-1?u?l?d?s' '?s?s?s'
- hashcat -a 6 -w4 -m 500 -O --username -i --opencl-device-types="1,2" -o results.txt new_to_crack.txt wordlists/words.txt '-1?u?l?d' '?s?d?d' 
- hashcat -w 4 -a 0 -m 500 -O -o results.txt --username -opencl-device-types="1,2" -r rules new_to_crack.txt wordlists/words.txt
# Help
- hashcat -I
- [hashcat cheatsheet](https://cheatsheet.haax.fr/passcracking-hashfiles/hashcat_cheatsheet/)