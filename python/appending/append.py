# add content to a file instead of writing over existing content, 
# you can open the file in append mode.
filename = './appendfile.txt'
with open(filename) as file_object:
    content = file_object.read()
    print(content)