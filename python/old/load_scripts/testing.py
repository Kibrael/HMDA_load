#prints the characters responsible for throwing errors.
#Theory: null values were used instead of NAs and populate as ASCII 0s. These need to be replaced with a string length 4, likely 'NA  '

with open('../dat/hmda1991_slice.dat') as f:
    lines = f.readlines()

for line in lines[4:5]:
    for char in line:
        print ord(char)