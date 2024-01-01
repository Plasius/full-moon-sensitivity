import os
import shutil

def move_and_rename_json_files(top_folder):
    for root, dirs, files in os.walk(top_folder):
        for file in files:
            if file.endswith(".json"):
                src_path = os.path.join(root, file)
                
                # Append the name of the folder to the JSON file
                folder_name = os.path.basename(root)
                new_file_name = f"{folder_name}_{file}"
                
                dest_path = os.path.join(top_folder, new_file_name)
                shutil.move(src_path, dest_path)
                
                print(f"Moved and renamed: {src_path} to {dest_path}")

# Replace 'Path/to/top/folder' with the actual path to your top folder
move_and_rename_json_files('/Users/plasius/Desktop/messages')
