# lets do a recap first
filename ="../pi.txt"
with open(filename) as file_object:
    content = file_object.read()
    print(content.rstrip())