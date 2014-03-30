from base64 import b64encode
import sys
from StringIO import StringIO

def read_file_to_buffer(filename):
	f = open(filename, "r")
	buf = StringIO(f.read())
	f.close()
	return buf

def print_image(filename):
	data = read_file_to_buffer(filename)
	sys.stdout.write("\033]1337;File=name=%s;size=%d;inline=1:%s\a\n" %
		(b64encode(filename), data.len, b64encode(data.getvalue())))
	data.close()

def push_file(filename):
	data = read_file_to_buffer(filename)
	sys.stdout.write("\033]1337;File=name=%s;size=%d;inline=0:%s\a\n" %
		(b64encode(filename), data.len, b64encode(data.getvalue())))
	data.close()
