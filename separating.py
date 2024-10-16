import os
import shutil

def separate_files_by_extension(source_folder):
    """
    Separates files in the source folder and all its subfolders into subfolders based on their file extensions.

    Parameters:
    source_folder (str): The path to the source folder containing the files to be separated.
    """
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"The source folder {source_folder} does not exist.")
        return

    # Walk through the directory tree
    for root, _, files in os.walk(source_folder):
        for file in files:
            # Get the file extension, excluding the dot
            file_extension = os.path.splitext(file)[1][1:]
            if not file_extension:  # Skip files without an extension
                continue

            # Create a folder for the file extension if it doesn't exist
            destination_folder = os.path.join(root, file_extension)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file to the appropriate folder
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_folder, file)
            try:
                shutil.move(source_file_path, destination_file_path)
            except Exception as e:
                print(f"Failed to move {file}: {e}")

    print("Files have been separated by extension.")

# Example usage
source_folder = '/Users/sujith/All in one/Courses/ZTM ML'
separate_files_by_extension(source_folder)
