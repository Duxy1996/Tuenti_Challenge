import sys
import binascii
import hashlib
# Usage:
# generate-password.php <user_id> <old_hash>

secret1 = 6533205
secret2 = 2340262
secret3 = 0

arg1 = sys.argv[1]
arg2 = 0
if(len(sys.argv) > 2):
		arg2 = sys.argv[2]


if((arg2 == 0)):
	# First password for this user
	print("First password for this user")
	secret3 = binascii.crc32(arg1) & 0xffffffff
else:
	# Existing user, password reset
	print("Existing user, password reset")
	secret3 = binascii.crc32(arg2) & 0xffffffff

print secret3

counter = secret3

for i in range(0,10000000):
	# This loop makes the passwords hard to reverse
	counter = (counter * secret1) % secret2

password = ""

for i in range(0,10):
	# Generate random passwords
	counter = (counter * secret1) % secret2
	con = counter % 94 +33	
	password = password + str(chr(con))

hashs = hashlib.md5()
hashs.update(password)
hashs = hashs.hexdigest()
print (password,hashs)

