#creates a test file using the data range that threw errors on load

with open('../dat/hmda1991.dat') as infile:
	lines = infile.readlines()

with open('../dat/hmda1991_slice.dat', 'w') as outfile:
	outfile.write(''.join(lines[3226037:3227000]))