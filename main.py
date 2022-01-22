# Write a Python program to merge two input files content into a single file

filenames = ['file1.txt', 'file2.txt']
with open('file3.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)