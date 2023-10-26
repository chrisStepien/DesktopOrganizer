# Python program to organize files on the desktop into folders

# importing required modules
import os  
import shutil
from pathlib import Path

# required paths
origin_path = Path('C:/Users/chris/OneDrive/Desktop')
destination_path = Path('C:/Users/chris/OneDrive/Desktop')

def main():
    
   unsorted_files = getting_files(origin_path)
   create_folders(destination_path, unsorted_files)
   setting_files(unsorted_files, destination_path)

# returns a list of all files in the given directory path         
def getting_files(directory: Path):     
    
    master_file_list = []
    
    for item in directory.iterdir():
        if item.is_file() and os.path.splitext(item)[-1].lower() != '.ini':
            
            master_file_list.append(item)
            
    return master_file_list

# creates a folder for each file format    
def create_folders(path, file_list):
    
    extension_list = []
    
    for file in file_list:
        
        # split the extension from the path and normalise it to lowercase
        file_ext = os.path.splitext(file)[-1].lower()
        extension_list.append(file_ext)

    # sorts out duplicates
    sorted_ext_list = sorted(set(extension_list))
    
    for ext in sorted_ext_list:
        
        # removes decimal from exstension and upper cases the remaining
        new_folder_path = path / (ext.replace('.', '').upper() + " Files")
        
        try:
            new_folder_path.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print("Folder is already there")
        else:
            print("Folder was created")        

# import files into folders
def setting_files(unsorted_files, path):
    
    for file in unsorted_files:
        
        # folder name for destination of current file
        folder_destination = os.path.splitext(file)[-1].replace('.','').upper() + " Files"
        # desktop path plus folder destination to get full path
        destination_path = path / folder_destination
        
        # moves files into correct folders
        shutil.move(file, destination_path)    
    

if __name__ == "__main__":
    main()    