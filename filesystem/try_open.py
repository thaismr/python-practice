

try:
    file = open('save_2.txt', 'w+')
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.seek(0)
    print(file.read())
finally:
    file.close()  # finally is always executed, so we make sure to close our file


with open('save_3.txt', 'a+') as file_2:
    file_2.write('Another Line\n')  # added to the END of the file ( a+ )
    file_2.seek(0)
    print(file_2.read())
    # Using WITH _____ AS ____ we don't need to CLOSE the file, as it does that for us
