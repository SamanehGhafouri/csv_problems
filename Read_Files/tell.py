# tell() : tell the current position that we are in the file
# because we already read 10 characters here this will
# will return 10
with open('test.txt', 'r') as f:

    size_to_read = 10
    f_contents = f.read(size_to_read)

    print(f.tell())