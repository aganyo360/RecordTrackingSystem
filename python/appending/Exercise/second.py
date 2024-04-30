# Infinite loop to prompt users for their name
while True:
    name = input("Please enter your name (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if name.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Greet the user
    print(f"Hello, {name}!")
    
    # Write their visit to guest_book.txt
    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")
        print("Your visit has been recorded in guest_book.txt.")
