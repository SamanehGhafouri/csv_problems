# copy picture files into a new file
# in order to work with picture files
# we need to open them in the binary mode
# we use 'rb', 'rw'
with open('pic.png', 'rb') as rf:
    with open('pic_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)