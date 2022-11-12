import hashlib
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-s", help="Hash type")
parser.add_argument("-c", help="Hash to crack")
parser.add_argument("-f", help="List supported cracking hash types", action="store_true")
parser.add_argument("-w", help="Wordlist to use for cracking")
parser.add_argument("-t", help="Specify amount of threads")
parser.add_argument("-e", "--example", help="To get a example", action="store_true")
parser.add_argument("-z", help="Help command", action="store_true")
# Process Arguments
args = parser.parse_args()

if args.z:
	parser.print_help()
	exit()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def typeHash(word):
	word = word.strip()
	if args.s == "md5":
		hashed_word = hashlib.md5(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "blake2b":
		hashed_word = hashlib.blake2b(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha512_256":
		hashed_word = hashlib.sha512_256(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha512_224":
		hashed_word = hashlib.sha512_224(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha3_384":
		hashed_word = hashlib.sha3_384(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha3_512":
		hashed_word = hashlib.sha3_512(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "shake_128":
		hashed_word = hashlib.shake_128(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "ripemd160":
		hashed_word = hashlib.ripemd160(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "whirlpool":
		hashed_word = hashlib.whirlpool(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha256":
		hashed_word = hashlib.sha256(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "shake_256":
		hashed_word = hashlib.shake_256(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha512":
		hashed_word = hashlib.sha512(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha224":
		hashed_word = hashlib.sha224(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sm3":
		hashed_word = hashlib.sm3(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "md4":
		hashed_word = hashlib.md4(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha3_224":
		hashed_word = hashlib.sha3_224(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha1":
		hashed_word = hashlib.sha1(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha3_256":
		hashed_word = hashlib.sha3_256(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "sha384":
		hashed_word = hashlib.sha384(word.encode()).hexdigest()
		return hashed_word
	elif args.s == "blake2s":
		hashed_word = hashlib.blake2s(word.encode()).hexdigest()
		return hashed_word
	else:
		print("Specify a valid hash mode.")
		parser.print_help()
		exit()


if len(sys.argv) < 2:
    parser.print_help()
    exit()

if args.example:
	print("Example: python3 main.py -c 527bd5b5d689e2c32ae974c6229ff785 -s md5 -w wordlist.txt")
	exit()

if args.f:
	print('''

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



		
		''')
	exit()

print('''


█──█ █▀▀█ █▀▀ █──█ ─█▀▀█ ▀▀█▀▀ ░█─▄▀ 
█▀▀█ █▄▄█ ▀▀█ █▀▀█ ░█▄▄█ ─░█── ░█▀▄─ 
▀──▀ ▀──▀ ▀▀▀ ▀──▀ ░█─░█ ─░█── ░█─░█
 - By MistyMan435 -
	''')
print("[+] CRACKING HASH ")

try:
	wordlist = open(str(args.w)).readlines()
except FileNotFoundError:
	print("Please specify wordlist file.")
	parser.print_help()
	exit()
for words in wordlist:
	words = words.strip()
	hashed_w = typeHash(words)
	if hashed_w == str(args.c):
		print(f"Hash Cracked: {words}")
		exit()
		continue
print("[!] Hash could not be cracked.")



