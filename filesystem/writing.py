# #
# Python: Writing to a file
# #

# Will CREATE OR --RESET-- the file and OPEN for read/write
file = open('save.txt', 'w+')
file.write('Line 1\n')
file.write('Line 2\n')
file.write('Line 3\n')

print('Can we read the file?')
print(file.read())  # anything to READ with CURSOR at the current point?

file.seek(0)     # get the CURSOR back to the TOP (0, 0) of the file!

print('Can we read the file?')
print(file.read())  # now we can read it from the top (0, 0)

file.seek(0)     # get the CURSOR back to the TOP (0, 0) of the file!

print(file.readline(), end='')      # read a single line
print(file.readline())              # read next line

file.seek(0)

print(file.readlines())     # get LINES as a LIST

file.seek(0)

for line in file.readlines():
    print(line, end='')

print('#' * 20)

# OR SIMPLY:
file.seek(0)

for line in file:
    print(line, end='')


file.close()  # ATTENTION: Never forget to CLOSE all open files
