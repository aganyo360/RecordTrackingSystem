# You can read an entire file or read the file line by line
# now let's open the file

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
