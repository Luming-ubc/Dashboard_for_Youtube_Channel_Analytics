# File objects

# Method 1: must close file
f = open('test.txt', 'r') # pass in name of the file, default is reading

print(f'The name of the file is "{f.name}"')
print(f'The mode of the file is "{f.mode}"')

f.close()  # close the file

# Method 2
# context manager, automatically close the file (if exceptions)
with open('test.txt', 'r') as f:

    for line in f:
        print(line, end='')

    # print(dir(f))
    # f_contents = f.readline()
    # print(f_contents, end='')

    # f_contents = f.readline()
    # print(f_contents)

    print(f.tell())
    f_contents = f.read(10)
    print(f_contents)

# writing to a file/ create a new file
with open('test2.txt', 'w') as f:
    print(dir(f))
    f.write('Test text 2!')

    f.write('\nWrite something more!')

# images use binary mode, 'b'
with open('image.png', 'rb') as rf:
    with open('image_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
