# # this is the first way in which we can read files from different dirs
# with open("../web/style.css") as file_object:
#     content = file_object.read()
#     print(content)

# # this is the second way in which we can read files from different dirs

file_path = 'C:\\Users\\BIGSMOKE\Documents\\tcp\sendingdatafiles\\File-Transfer-Using-TCP-Socket-in-C-Socket-Programming\\file2.txt'
with open(file_path) as file_object:
    content= file_object.read()
    print(content)