# Iterating through the file

with open('test.txt', 'r') as f:

    # iterating through the file and print
    # the content line by line without space using end=''
    for line in f:
        print(line, end='')

    # print the first 100 character in the file
    f_content = f.read(100)
    print(f_content)