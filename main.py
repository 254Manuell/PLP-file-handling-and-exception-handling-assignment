def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ")
        
        with open(filename, "r") as file:
            content = file.read()
        
        modified_content = content.upper()
        
        new_filename = f"modified_{filename}"
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
        print(f"File successfully modified and saved as '{new_filename}'")
    
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Please check file permissions.")

read_and_modify_file()
