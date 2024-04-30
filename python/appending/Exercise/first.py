
with open('./guests.txt','a') as file_object:
    name = input('Enter your name:')
    file_object.write(name)