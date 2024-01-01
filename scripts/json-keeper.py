import os

def delete_non_json_files(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if not filename.endswith('.json'):
                # Delete files that are not JSON
                os.remove(file_path)
                print(f"Deleted: {file_path}")

root_folder = '/Users/plasius/Desktop/messages'

delete_non_json_files(root_folder)