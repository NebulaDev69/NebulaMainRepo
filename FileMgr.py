import os
import shutil
import sys

class FileManager:
    def __init__(self):
        self.current_dir = os.getcwd()

    def list_files(self):
        """Lists the files in the current directory."""
        try:
            print(f"Current directory: {self.current_dir}")
            files = os.listdir(self.current_dir)
            if not files:
                print("Directory is empty.")
            for index, file in enumerate(files, 1):
                print(f"{index}. {file}")
        except Exception as e:
            print(f"Error listing files: {e}")

    def change_directory(self):
        """Change the current directory."""
        dir_path = input("Enter directory path: ")
        if os.path.isdir(dir_path):
            self.current_dir = dir_path
        else:
            print(f"'{dir_path}' is not a valid directory.")

    def move_file(self):
        """Move a file from one location to another."""
        source_file = input("Enter the file to move: ")
        if os.path.exists(source_file):
            destination = input("Enter destination directory: ")
            if os.path.isdir(destination):
                shutil.move(source_file, destination)
                print(f"Moved {source_file} to {destination}")
            else:
                print(f"'{destination}' is not a valid directory.")
        else:
            print(f"'{source_file}' does not exist.")

    def copy_file(self):
        """Copy a file from one location to another."""
        source_file = input("Enter the file to copy: ")
        if os.path.exists(source_file):
            destination = input("Enter destination directory: ")
            if os.path.isdir(destination):
                shutil.copy(source_file, destination)
                print(f"Copied {source_file} to {destination}")
            else:
                print(f"'{destination}' is not a valid directory.")
        else:
            print(f"'{source_file}' does not exist.")

    def delete_file(self):
        """Delete a file."""
        file_to_delete = input("Enter the file to delete: ")
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)
            print(f"Deleted {file_to_delete}")
        else:
            print(f"'{file_to_delete}' does not exist.")

    def show_menu(self):
        """Display the menu and take user input for actions."""
        while True:
            print("\n===== File Manager =====")
            print("1. List files in current directory")
            print("2. Change directory")
            print("3. Move file")
            print("4. Copy file")
            print("5. Delete file")
            print("6. Exit")
            choice = input("Choose an action: ")

            if choice == "1":
                self.list_files()
            elif choice == "2":
                self.change_directory()
            elif choice == "3":
                self.move_file()
            elif choice == "4":
                self.copy_file()
            elif choice == "5":
                self.delete_file()
            elif choice == "6":
                print("Exiting File Manager.")
                sys.exit(0)
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.show_menu()
