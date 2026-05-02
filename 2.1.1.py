# Initialize empty list
lst = []

while True:
    # Display menu
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")
    
    choice = input("Enter choice: ")
    
    # Add
    if choice == '1':
        try:
            num = int(input("Integer: "))
            lst.append(num)
            print("List after adding:", lst)
        except:
            print("Invalid input")
    
    # Remove
    elif choice == '2':
        if not lst:
            print("List is empty")
        else:
            try:
                num = int(input("Integer: "))
                if num in lst:
                    lst.remove(num)
                    print("List after removing:", lst)
                else:
                    print("Element not found")
            except:
                print("Invalid input")
    
    # Display
    elif choice == '3':
        if not lst:
            print("List is empty")
        else:
            print(lst)
    
    # Quit
    elif choice == '4':
        break
    
    # Invalid choice
    else:
        print("Invalid choice")
