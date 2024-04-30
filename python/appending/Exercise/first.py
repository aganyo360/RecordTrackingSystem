name = input("Enter your name:\n")
with open("guests.txt",'a') as file_object:
    file_object.write(name)
    print('Your name has been written to guests.txts')