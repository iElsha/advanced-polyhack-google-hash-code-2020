from FileManager import *
import sys

def main(path_to_file):
	data = parse(path_to_file)

	output(path_to_file, data)


if __name__ == '__main__':
	for arg in sys.argv[1:]:
		main(arg)
