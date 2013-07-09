from optparse import OptionParser
import sys
import pandas as pd

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
	parser.add_option(
			"-t", "--test-data",
			help="Prepare the input as test data ",
			action="store_true", dest='test_data')

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
	format_csv(infile, sys.stdout, options.test_data)

	## Close the infile iff not stdin
	if infilename:
		infile.close()

def format_csv(infile, outfile, test_data):
	if test_data:
		inlabels = ["Sex", "Age", "Pclass", "Fare", "Cabin", "SibSp", "Parch", "Embarked"]
		outlabels = "PassengerId,IsFemale,Age,Pclass,Fare,Cabin,SibSp,Parch,Embarked\n"
	else:
		inlabels = ["Survived", "Sex", "Age", "Pclass", "Fare", "Cabin", "SibSp", "Parch", "Embarked"]
		outlabels = "Survived,IsFemale,Age,Pclass,Fare,Cabin,SibSp,Parch,Embarked\n"

	df = pd.read_csv(infile, index_col="PassengerId")[inlabels]
	df["Sex"] = df["Sex"].map(lambda x: 1 if x == "female" else 0)
	df["Cabin"] = df[~pd.isnull(df["Cabin"])]["Cabin"].map(lambda x: list('ABCDEFGT').index(list(x)[0]))
	df["Embarked"] = df[~pd.isnull(df["Embarked"])]["Embarked"].map(lambda x: list('CQS').index(list(x)[0]))
	outfile.write(outlabels)

	# only show the index (PassengerId) if it's test data b/c we need to identify that
	df.to_csv(outfile, header=False, index=test_data)

if __name__=='__main__':
	main()
