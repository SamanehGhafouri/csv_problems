# copy the test.txt file into the new file named test_copy.txt

with open('../Read_Files/test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

