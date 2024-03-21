# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 5678\n")
        print("File 'my_file.txt' created and initial content written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        file_contents = file.read()
        print("Contents of 'my_file.txt':")
        print(file_contents)
except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")
except PermissionError:
    print("Error: Permission denied while trying to read 'my_file.txt'.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending a new line\n")
        file.write("7890\n")
        file.write("One more line added in append mode\n")
        print("Additional content appended to 'my_file.txt'.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File appending process completed.")
