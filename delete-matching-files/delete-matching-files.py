import os

def delete_copied_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith("(1).jpg"):  # Adjust the file extension as needed
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

if __name__ == "__main__":
    folder_to_scan = r"C:\path\to\your\folder"  # Replace with the actual folder path
    delete_copied_files(folder_to_scan)
