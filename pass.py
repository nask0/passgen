#passgen#
import sys, random, string

def lowercase():
	while True:
		try:
			char_set = string.ascii_lowercase
			result = ''.join(random.sample(char_set*6, 8))
			print result
		except (KeyboardInterrupt):
			exit()
def lowerupper():
	while True:
		try:
			char_set = string.ascii_lowercase + string.ascii_uppercase
			result = ''.join(random.sample(char_set*6, 8))
			print result
		except (KeyboardInterrupt):
			exit()
def lowernum():
	while True:
		try:
			char_set = string.ascii_lowercase + string.digits
			result = ''.join(random.sample(char_set*6, 8))
			print result
		except (KeyboardInterrupt):
			exit()
def uppernum():
	while True:
		try:
			char_set = string.ascii_uppercase + string.digits
			result = ''.join(random.sample(char_set*6, 8))
			print result
		except (KeyboardInterrupt):
			exit()
def loweruppernum():
	while True:
		try:
			char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
			result = ''.join(random.sample(char_set*6, 8))
			print result
		except (KeyboardInterrupt):
			exit
def arglist():
	print 'options: -l lowercase, -lU lower and uppercase, -l1 lower and numerals, -U1 upper and numerals, -lU1 lower, upper, and numerals, --help this list'

args = sys.argv[1:]
if args:
	for arg in args:
		if arg == '-l':
			lowercase()
		elif arg == '-lU':
			lowerupper()
		elif arg == '-l1':
			lowernum()
		elif arg == '-U1':
			uppernum()
		elif arg == '-lU1':
			loweruppernum()
		elif arg == '--help':
			arglist()
else:
	arglist()
