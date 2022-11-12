
# HashATK

HashATK is a hash cracker made purely from python3 that can crack hashes in seconds.



## Support Hash Modes

- blake2b
- sha512_256
- sha512_224
- md5-sha1
- sha3_384
- md5
- sha3_512
- shake_128
- ripemd160
- whirlpool
- sha256
- shake_256
- sha512
- sha224
- sm3
- md4
- sha3_224
- sha1
- sha3_256
- sha384
- blake2s


## Deployment

Very easy to run only one command.

```bash
  python3 main.py
```
    
## Usage/Examples


```bash
# python3 main.py -c 527bd5b5d689e2c32ae974c6229ff785 -s md5 -w wordlist.txt

█──█ █▀▀█ █▀▀ █──█ ─█▀▀█ ▀▀█▀▀ ░█─▄▀ 
█▀▀█ █▄▄█ ▀▀█ █▀▀█ ░█▄▄█ ─░█── ░█▀▄─ 
▀──▀ ▀──▀ ▀▀▀ ▀──▀ ░█─░█ ─░█── ░█─░█
 - By MistyMan435 -
	
[+] CRACKING HASH 
Hash Cracked: john


```
List supported modes
```bash
# python3 main.py -f

--- Available Hash Modes ---

- blake2b
- sha512_256
- sha512_224
- md5-sha1
- sha3_384
- md5
- sha3_512
- shake_128
- ripemd160
- whirlpool
- sha256
- shake_256
- sha512
- sha224
- sm3
- md4
- sha3_224
- sha1
- sha3_256
- sha384
- blake2s


```
Example command
```bash
# python3 main.py -e

█──█ █▀▀█ █▀▀ █──█ ─█▀▀█ ▀▀█▀▀ ░█─▄▀ 
█▀▀█ █▄▄█ ▀▀█ █▀▀█ ░█▄▄█ ─░█── ░█▀▄─ 
▀──▀ ▀──▀ ▀▀▀ ▀──▀ ░█─░█ ─░█── ░█─░█
 - By MistyMan435 -
	
[+] CRACKING HASH 
Hash Cracked: john


```
List all commands

```bash
# python3 main.py -z

usage: main.py [-h] [-s S] [-c C] [-f] [-w W] [-t T] [-e] [-z]

optional arguments:
  -h, --help     show this help message and exit
  -s S           Hash type
  -c C           Hash to crack
  -f             List supported cracking hash types
  -w W           Wordlist to use for cracking
  -t T           Specify amount of threads
  -e, --example  To get a example
  -z             Help command


```

## Note

I, the author, is not responsible with any actions done with this script.
## Roadmap

- More supported modes



