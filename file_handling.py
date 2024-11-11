# file_handling_assignment.py

def main():
    filename = "my_file.txt"
    
    # File Creation
    try:
        with open(filename, 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is my first line.\n")
            file.write("Here is a number: 42\n")
        print("File created and initial content written.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while creating the file: {e}")
    finally:
        print("File creation attempt completed.")

    # File Reading and Display
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        print("File reading attempt completed.")

    # File Appending
    try:
        with open(filename, 'a') as file:
            file.write("Appending a new line.\n")
            file.write("Adding another line with a number: 99\n")
            file.write("Final line in the file.\n")
        print("Additional content appended to the file.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("File appending attempt completed.")

if __name__ == "__main__":
    main()
