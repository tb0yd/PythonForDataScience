from optparse import OptionParser
import sys

def main():

	r"""
	DESCRIPTION
	-----------
	Deletes every nth line of a file or stdin, starting with the
	first line, print to stdout.

	EXAMPLES
	--------
	Delete every second line of a file
	python deleter.py -n 2 infile.csv
	"""
	usage = "usage: %prog [options] dataset"
	usage += '\n'+main.__doc__
	parser = OptionParser(usage=usage)
	parser.add_option(
			"-n", "--deletion_rate",
			help="Delete every nth line [default: %default] ",
			action="store", dest='deletion_rate', type=float, default=2)

	(options, args) = parser.parse_args()

	### Parse args
	# Raise an exception if the length of args is greater than 1
	assert len(args) <= 1
	infilename = args[0] if args else None

	## Get the infile
	if infilename:
		infile = open(infilename, 'r')
	else:
		infile = sys.stdin

	## Call the function that does the real work
	delete(infile, sys.stdout, options.deletion_rate)

	## Close the infile iff not stdin
	if infilename:
		infile.close()

def delete(infile, outfile, deletion_rate):
	"""
	Write later, if module interface is needed.
	"""

	for linenumber, line in enumerate(infile):
		if linenumber % deletion_rate != 0:
			outfile.write(line)

if __name__=='__main__':
	main()
