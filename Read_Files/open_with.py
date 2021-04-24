# Open with
# context manager

with open('test.txt', 'r') as f:

    # just read whatever is in the file
    f_contents = f.read()
    print(f_contents)

    # print the content of the file in a list
    f_content_lines = f.readlines()
    print(f_content_lines)

    # print the first line of the file
    f_line = f.readline()
    print(f_line, end='')

    f_line = f.readline()
    print(f_line, end='')











