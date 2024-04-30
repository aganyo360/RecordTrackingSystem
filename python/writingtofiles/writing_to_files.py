
# lets explain the code below
filename = './write_file.txt'
with open(filename, "w") as file_object:
    file_object.write( ' I am learnning reading and writing to files\n this should create a new line\n it just work \n this is the fourth line')

#  at line 3 we create a variable to contain file path
# open( filename, "w") the 'w' makes it to a read mode
