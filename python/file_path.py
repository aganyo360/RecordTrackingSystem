# this is the first way in which we can read files from different dirs
with open("../web/style.css") as file_object:
    content = file_object.read()
    print(content)