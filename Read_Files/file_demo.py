# Open File

# reading the file 'r'
# writing 'w'
# appending 'a'
# read and write 'r+'

f = open('test.txt', 'r')

# print the name of the file
print(f.name)

# print the mode of the file like if it is open to read
# it will print 'r'
print(f.mode)

f.close()
