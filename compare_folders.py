import os
import sys

def get_folder_info(folder_path):
    subfolder_count = 0
    file_count = 0
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(folder_path):
        subfolder_count += len(dirnames)
        file_count += len(filenames)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)

    return subfolder_count, file_count, total_size

def compare_folders(folder1, folder2):
    # Define paths
    downloads_folder = os.path.expanduser("~/Downloads")
    folder1_path = os.path.join(downloads_folder, folder1)
    folder2_path = os.path.join(downloads_folder, folder2)

    if not os.path.isdir(folder1_path) or not os.path.isdir(folder2_path):
        print("One or both specified folders do not exist in the Downloads folder.")
        sys.exit(1)

    # Gather folder information
    folder1_subfolders, folder1_files, folder1_size = get_folder_info(folder1_path)
    folder2_subfolders, folder2_files, folder2_size = get_folder_info(folder2_path)

    # Print results
    print(f"\nFolder: {folder1}")
    print(f"  Subfolders: {folder1_subfolders}")
    print(f"  Files: {folder1_files}")
    print(f"  Total Size: {folder1_size / (1024 ** 2):.2f} MB")

    print(f"\nFolder: {folder2}")
    print(f"  Subfolders: {folder2_subfolders}")
    print(f"  Files: {folder2_files}")
    print(f"  Total Size: {folder2_size / (1024 ** 2):.2f} MB")

    # Determine latest version
    if (
        folder1_size > folder2_size
        and folder1_subfolders >= folder2_subfolders
        and folder1_files >= folder2_files
    ):
        latest_folder = folder1
    elif (
        folder2_size > folder1_size
        and folder2_subfolders >= folder1_subfolders
        and folder2_files >= folder1_files
    ):
        latest_folder = folder2
    else:
        latest_folder = "Inconclusive based on criteria"

    print(f"\nLatest version (based on criteria): {latest_folder}")

# Run the script
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_folders.py <folder1_name> <folder2_name>")
    else:
        folder1_name = sys.argv[1]
        folder2_name = sys.argv[2]
        compare_folders(folder1_name, folder2_name)
