# open both files

with open('first.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
    #append content from first file
    for line in firstfile:
        #append content to secondfile
        secondfile.write(line)