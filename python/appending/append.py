# add content to a file instead of writing over existing content, 
# you can open the file in append mode.
filename = './appendfile.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nthis is the apppend document")
    