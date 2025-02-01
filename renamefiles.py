import os


def rename_files_in_folder(folder_path):
    # Get the folder name
    folder_name = os.path.basename(folder_path)

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(
        os.path.join(folder_path, f))]

    # Sort files to ensure consistent renaming order
    files.sort()

    # Rename each file
    for index, filename in enumerate(files, start=1):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # Create the new file name
        new_filename = f"{folder_name} {index}{file_extension}"

        # Get the full paths for the old and new file names
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")


if __name__ == "__main__":
    # Ask the user for the folder path
    folder_path = input(
        "Enter the full path to the folder containing the files: ").strip()

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
    else:
        # Call the function to rename files
        rename_files_in_folder(folder_path)
