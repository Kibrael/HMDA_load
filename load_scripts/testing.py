with open('../dat/hmda1991_slice.dat') as f:
    lines = f.readlines()

for line in lines[4:5]:
    for char in line:
        print ord(char)